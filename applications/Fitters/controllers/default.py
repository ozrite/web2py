# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    page = 'home'
    if session.a is None:
        session.a = 1
    else:
        session.a = session.a + 1

    # response.flash = T("Hello World")
    # response.flash = session.a
    # return dict(message=T('Welcome to web2py!'))
    return locals()

def test():
#     return "<h2>hello test</h2>"
    xenv  = request.env.http_accept_language
    yargs = request.args
    zvars = request.vars
    return locals()
#     return "<h1>%s</h1>" %x
#     return {'a':1,'b':2}

def subview1():
    msg="this msg is coming from subview1 controller"
    return locals()

def men():
    page = 'men'
    msg = "welcome to Fitters Men"
    name = request.vars.your_name
    # redirect(URL('women'))
    # redirect(URL('women',args=[1,4,6]))
    #redirect(URL('women',args=[1,4,6], vars={'a':'test','b':'hello','c': 78}))
    return locals()

def women():
    page = 'women'
    # x = request.args
    msg = "welcome to Fitters Women"
    return locals()

def mini():
    page = 'mini'
    msg = "welcome to Fitters mini"
    # redirect(URL('men'))
    form = SQLFORM.factory(Field('your_name')).process()
    if form.accepted:
        redirect(URL('men',vars={'your_name':form.vars.your_name}))
    return locals()

def unstitched():
    page = 'unstitched'
    #msg = "welcome to unstitched"
    # form = SQLFORM(db.blog_post).process()
    # rows = db(db.blog_post).select()
    grid = SQLFORM.grid(db.blog_post)
    return locals()

def accessories():
    page = 'accessories'
    msg = "welcome to accessories"
    return locals()

def business():
    page = 'business'
    msg = "welcome to Fitters Business"
    return locals()

def overseas():
    page = 'overseas'
    msg = "welcome to Fitters Overseas"
    return locals()

def prices():
    page = 'prices'
    msg = "welcome to prices"

    yargs = request.args(0)
    return locals()

def offers():
    page = 'offers'
    msg = "welcome to offers"
    return locals()

def quickorder():
    page = 'quickorder'
    msg = "welcome to Quick Order"
    return locals()

def about():
    page = 'about'
    msg = "welcome to AboutUs"
    return locals()

def contact():
    page = 'contact'
    msg = "welcome to contactus"
    return locals()

def videos():
    page = 'videos'
    msg = "videos"
    return locals()

def jobs():
    page = 'jobs'
    msg = "welcome to jobs"
    return locals()

def faq():
    page = 'faq'
    msg = "welcome to faq"
    return locals()

def privacy():
    page = 'privacy'
    msg = "welcome to privacy"
    return locals()

def terms():
    page = 'terms'
    msg = "welcome to terms"
    return locals()

def cancelation():
    page = 'cancelation'
    msg = "welcome to cancelation"
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
