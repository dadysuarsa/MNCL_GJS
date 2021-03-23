# -*- coding: utf-8 -*-

import babel.dates
import re
import werkzeug
import math
from werkzeug.datastructures import OrderedMultiDict

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import fields, http, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.tools.misc import get_lang
from odoo.osv import expression



class WebsiteServicesController(http.Controller):
    _data_per_page = 30
    _pager_max_pages = 5

    @http.route(['''/serviskami/<model("services.website.mnc", "[('website_id', 'in', (False, current_website_id))]"):services>'''], type='http', auth="public", website=True, sitemap=False)
    def services_detail(self, services, **post):
        if not services.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()
        values = {
            'services': services,
        }
        return request.render("mnc_x_gjs_website.services_detail", values)

class WebsiteNewsController(http.Controller):
    _data_per_page = 30
    _pager_max_pages = 5

    @http.route(['''/berita/<model("news.website.mnc", "[('website_id', 'in', (False, current_website_id))]"):news>'''], type='http', auth="public", website=True, sitemap=False)
    def news_detail(self, news, **post):
        if not news.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()
        values = {
            'news': news,
        }
        return request.render("mnc_x_gjs_website.news_detail", values)


class WebsiteCarrierController(http.Controller):
    _data_per_page = 30
    _pager_max_pages = 5

    @http.route(['''/karir/<model("carrier.website.mnc", "[('website_id', 'in', (False, current_website_id))]"):carrier>'''], type='http', auth="public", website=True, sitemap=False)
    def services_detail(self, carrier, **post):
        if not carrier.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()
        values = {
            'carrier': carrier,
        }
        return request.render("mnc_x_gjs_website.carrier_detail", values)
