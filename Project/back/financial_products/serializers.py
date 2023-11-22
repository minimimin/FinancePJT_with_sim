from rest_framework import serializers
from .models import FinancialCompany, DepositProduct, DepositProductOptions, SavingProduct, SavingProductOptions, LoanForHome, LoanForHomeOptions

# 금융회사---------------------------------------------------------------------------------------------
class FinancialCompanySerializer(serializers.ModelSerializer):
    class Meta():
        model = FinancialCompany
        fields = '__all__'


# 예금-----------------------------------------------------------------------------------------------------------------------------
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositProduct
        fields = '__all__'


class DepositProductOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositProductOptions
        fields = '__all__'


class DepositProductWithOptionsSerializer(serializers.ModelSerializer):
    deposit_product_option = DepositProductOptionsSerializer(many=True, read_only=True)

    class Meta():
        model = DepositProduct
        fields = '__all__'


# 적금----------------------------------------------------------------------------------------------------------------------------- 
class SavingProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = SavingProduct
        fields = '__all__'


class SavingProductOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = SavingProductOptions
        fields = '__all__'


class SavingProductWithOptionsSerializer(serializers.ModelSerializer):
    saving_product_option = SavingProductOptionsSerializer(many=True, read_only=True)

    class Meta():
        model = SavingProduct
        fields = '__all__'


# 전세자금대출-------------------------------------------------------------------------------------------------------------
class LoanForHomeSerializer(serializers.ModelSerializer):
    class Meta():
        model = LoanForHome
        fields = '__all__'

class LoanForHomeOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = LoanForHomeOptions
        fields = '__all__'

class LoanForHomeWithOptionsSerializer(serializers.ModelSerializer):
    loan_home_product_option = LoanForHomeOptionsSerializer(many=True, read_only=True)

    class Meta():
        model = LoanForHome
        fields = '__all__'


