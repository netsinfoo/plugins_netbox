import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn

from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ


class RegisterTable(BaseTable):
    pk = ToggleColumn()
    ip = tables.LinkColumn(
        viewname='plugins:sdns:register',
        args=[Accessor('pk')]
    )
    domain = tables.LinkColumn(
        viewname='plugins:sdns:domain',
        args=[Accessor('pk')]
    )
    class Meta(BaseTable.Meta):
        model = Register
        fields = (
            'pk',
            'ip',
            'host',
            'domain',
        )

class RegisterdTable(BaseTable):
    pk = ToggleColumn()
    ip = tables.LinkColumn(
        viewname='plugins:sdns:register',
        args=[Accessor('pk')]
    )    
   
    class Meta(BaseTable.Meta):
        model = Register
        fields = (
            'pk',
            'ip',
            'host',
        )

# ============ DOMAIN ==========================

class DomainTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:domain',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Domain
        fields = (
            'pk',
            'name',
            'date_joined',
            'owner',
            'domParent',
        )

class DomcTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:domain',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Domain
        fields = (
            'pk',
            'name',
        )



# ============ Resp ==========================

class RespTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:resp_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Resp
        fields = (
            'pk',
            'name',
            'tipo',
            'dom',
        )


class RespDTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:resp',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Resp
        fields = (
            'pk',
            'name',
            )



# ============ Ns ==========================

class NsTable(BaseTable):
    pk = ToggleColumn()
    ns = tables.LinkColumn(
        viewname='plugins:sdns:ns_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Ns
        fields = (
            'pk',
            'ns',
            'tipo',
            'dom',
        )


class NsdTable(BaseTable):
    pk = ToggleColumn()
    ns = tables.LinkColumn(
        viewname='plugins:sdns:ns_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Ns
        fields = (
            'pk',
            'ns',
            'tipo',
        )



# ============ Mx ==========================

class MxTable(BaseTable):
    pk = ToggleColumn()
    mx = tables.LinkColumn(
        viewname='plugins:sdns:mx_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Mx
        fields = (
            'pk',
            'mx',
            'prior',
            'dom',
        )


class MxdTable(BaseTable):
    pk = ToggleColumn()
    mx = tables.LinkColumn(
        viewname='plugins:sdns:mx_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Mx
        fields = (
            'pk',
            'mx',
            'prior',
        )

# ============ Cts ==========================

class CtsTable(BaseTable):
    pk = ToggleColumn()
    registro = tables.LinkColumn(
        viewname='plugins:sdns:cts_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Resp
        fields = (
            'pk',
            'registro',
            'reg',
            'content',
        )


class CtscTable(BaseTable):
    pk = ToggleColumn()
    content = tables.LinkColumn(
        viewname='plugins:sdns:cts_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Cts
        fields = (
            'pk',
            'content',
        )
# ============ DomainServ ==========================

class DomainServTable(BaseTable):
    pk = ToggleColumn()
    service = tables.LinkColumn(
        viewname='plugins:sdns:domainserv_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = DomainServ
        fields = (
            'pk',
            'service',
            'dominio',
            'relation',
        )
