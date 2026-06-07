# testapp/serializers.py (もしくは該当する serializers.py)
from rest_framework import serializers


class CustomerQuerySerializer(serializers.Serializer):
    shop_id = serializers.CharField(max_length=100)
    customer_id = serializers.CharField(max_length=100)
    # 送信先選択用のフィールドを追加（デフォルト値は 'none'）
    action_type = serializers.ChoiceField(
        choices=[("A", "商用先"), ("B", "商接先"), ("none", "保存のみ")],
        default="none",
        required=False,
    )
