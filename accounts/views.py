from rest_framework.views import APIView, status, Request, Response

from accounts.models import Account
from users.permissions import CustomPermission
from accounts.serializers import AccountSerializer

class AccountView(APIView): 
  def get(self, request) -> Response:
        users = Account.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AccountDetailView(APIView):

  def get(self, request, account_id) -> Response:
    try:
        account = Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        return Response({"message": "Conta nao encontrada"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_200_OK)