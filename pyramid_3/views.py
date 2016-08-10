from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
@view_config(route_name='gsi', renderer='templates/mytemplate_gsi.pt')
def my_view(request):
    return {'project': 'Pyramid_3'}
