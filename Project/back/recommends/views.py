import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from financial_products.models import DepositProduct, SavingProduct, LoanForHome
from financial_products.serializers import DepositProductSerializer, SavingProductSerializer, LoanForHomeSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommend_product(request):
    if request.method == 'POST':
        # 나의 user id 가져오기
        my_id = request.data['user']['id']

        # 모든 유저 정보를 가져와 DataFrame으로 변환
        all_users = Profile.objects.all().values()
        df_users = pd.DataFrame.from_records(all_users)

        # Null 값을 0으로 채우기
        df_users.fillna(0, inplace=True)

        # 직업 매핑
        df_users['job'] = df_users['job'].map({'학생 및 주부': 1, '사업가 및 프리랜서': 2, '회사원': 3, '기타': 4})

        # 주거래은행 매핑
        df_users['main_bank'] = df_users['main_bank'].map({
            '우리은행': 1, '한국스탠다드차타드은행': 2, '대구은행': 3, '부산은행': 4, '광주은행': 5,
            '제주은행': 6, '전북은행': 7, '경남은행': 8, '중소기업은행': 9, '한국산업은행': 10,
            '국민은행': 11, '신한은행': 12, '농협은행주식회사': 13, '하나은행': 14,
            '주식회사 케이뱅크': 15, '수협은행': 16, '주식회사 카카오뱅크': 17, '토스뱅크 주식회사': 18
        })

        # 선호은행상품 매핑
        df_users['banking_products'] = df_users['banking_products'].map({
            '예금': 1, '적금': 2, '대출': 3, '해당없음': 4
        })

        # 선호카드상품 매핑
        df_users['card_products'] = df_users['card_products'].map({
            '신용카드': 1, '체크카드': 2, '해당없음': 3
        })

        # 사용자가 선택한 필드만 유사도를 계산
        selected_columns = request.data['selected']
        df_users_with_selected_columns = df_users[selected_columns].dropna()
        # print(df_users_with_selected_columns)

        # 유사도 계산 (여기에서는 cosine_similarity를 사용했습니다)
        similarities = cosine_similarity(df_users_with_selected_columns.values)

        # 현재 사용자와의 유사도 가져오기
        user_similarities = similarities[my_id-2]

        # 상위 50개 유사한 사용자 가져오기
        similar_users_index = user_similarities.argsort()[-2:-52:-1]

        # 상위 50개 유사한 사용자의 프로필 정보 가져오기
        similar_users_profiles = df_users.iloc[similar_users_index]

        # user_id 열의 값만 가져와서 리스트로 저장
        user_ids_list = similar_users_profiles['user_id'].tolist()

        # 각 유저의 deposit_products, saving_products, loan_home_products 빈도수 계산
        deposit_counts = Counter()
        saving_counts = Counter()
        loan_home_counts = Counter()

        for user_id in user_ids_list:
            user_profile = Profile.objects.get(user_id=user_id)
            deposit_counts.update(user_profile.deposit_products.values_list('id', flat=True))
            saving_counts.update(user_profile.saving_products.values_list('id', flat=True))
            loan_home_counts.update(user_profile.loan_home_products.values_list('id', flat=True))

        # 각 외래키에 해당하는 객체의 정보 가져오기
        deposit_products_info = DepositProduct.objects.filter(id__in=deposit_counts.keys())
        saving_products_info = SavingProduct.objects.filter(id__in=saving_counts.keys())
        loan_home_products_info = LoanForHome.objects.filter(id__in=loan_home_counts.keys())

        # 빈도수가 많은 순으로 정렬
        sorted_deposit_products_info = sorted(deposit_products_info, key=lambda x: deposit_counts[x.id], reverse=True)[:10]
        sorted_saving_products_info = sorted(saving_products_info, key=lambda x: saving_counts[x.id], reverse=True)[:10]
        sorted_loan_home_products_info = sorted(loan_home_products_info, key=lambda x: loan_home_counts[x.id], reverse=True)[:10]

        # 객체를 serializer로 변환
        result_data = [
            {'sorted_deposit_products_info': DepositProductSerializer(sorted_deposit_products_info, many=True).data},
            {'sorted_saving_products_info': SavingProductSerializer(sorted_saving_products_info, many=True).data},
            {'sorted_loan_home_products_info': LoanForHomeSerializer(sorted_loan_home_products_info, many=True).data},
        ]

        # Vue로 전송
        return Response(result_data)