from rest_framework.serializers import ModelSerializer
from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ

class RegisterSerializer(ModelSerializer):
    
    class Meta:
        model = Register
        fields = ('ip', 'host', 'domain')

class DomainSerializer(ModelSerializer):
    
    class Meta:
        model = Domain
        fields = ('owner', 'name', 'date_joined', 'domParent')

class RespSerializer(ModelSerializer):
    
    class Meta:
        model = Resp
        fields = ('dom', 'name', 'tipo')

class NsSerializer(ModelSerializer):
    
    class Meta:
        model = Ns
        fields = ('dom', 'ns', 'tipo')

class MxSerializer(ModelSerializer):
    
    class Meta:
        model = Mx
        fields = ('dom', 'mx', 'prior')

class CtsSerializer(ModelSerializer):
    
    class Meta:
        model = Cts
        fields = ('registro', 'reg', 'content')

class DomainServSerializer(ModelSerializer):
    
    class Meta:
        model = DomainServ
        fields = ('service', 'dominio', 'relation')