# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def example(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))  #arrastramos el request para pasar datos de la sesion


def example2(request):
    return render_to_response('index2.html',
                              context_instance=RequestContext(request))  #arrastramos el request para pasar datos de la sesion
