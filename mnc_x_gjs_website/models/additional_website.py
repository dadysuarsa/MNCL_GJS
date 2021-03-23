# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.http_routing.models.ir_http import slug


class servicesdetailgaleryswebsitemnc(models.Model):
    _name = 'servicesdetailgalery.website.mnc'
    
    sequence = fields.Integer(string="Sequence")
    servicesdetailgalery_images_fname = fields.Char(string="Images Galery Name")
    servicesdetailgalery_images = fields.Binary(string="Galery Images")
    serviceswebsitemnc_id = fields.Many2one('services.website.mnc')
    
class serviceswebsitemnc(models.Model):
    _name = 'services.website.mnc'
    _inherit = ['website.seo.metadata', 'website.published.multi.mixin']
    _rec_name = 'services_name'
    _order = 'sequence'
    
    # plan
    sequence = fields.Integer(string="Sequence")
    services_name = fields.Char(string="Name Services")
    services_description = fields.Text(string="Description Services")
    services_images = fields.Binary(string="Images Services")
    services_images_fname = fields.Char(string="Images Services Name")
    website_id = fields.Many2one('website')
    
    
    services_detail_images = fields.Binary(string="Images Services")
    services_detail_images_fname = fields.Char(string="Images Services Name")
    services_images_url = fields.Char(string="Images Services URL")
    services_images_attachment_id = fields.Many2one('ir.attachment', string="Images Services Attachment ID")
    
    services_detail_description = fields.Text(string="Description Services")
    services_detail_description_2 = fields.Text(string="Description Services 2")
    service_detail_galery = fields.One2many('servicesdetailgalery.website.mnc', 'serviceswebsitemnc_id', string='Service Detail Gallery')
    
    
    @api.depends('services_name')
    def _compute_website_url(self):
        super(serviceswebsitemnc, self)._compute_website_url()
        for services in self:
            if services.id:  # avoid to perform a slug on a not yet saved record in case of an onchange.
                services.website_url = '/serviskami/%s' % slug(services)
                
                
    @api.onchange('services_detail_images')
    def onchange_attachments_data(self):
        if self.services_images_attachment_id:
            get_attachment_id = self.env['ir.attachment'].search([('id', '=', self.services_images_attachment_id.id)])
            get_attachment_id.write({'datas': self.services_detail_images,'name': self.services_detail_images_fname})
        else:
            attachmentid = self.env['ir.attachment'].create({
                'name': self.services_detail_images_fname,
                'type': 'binary',
                'datas': self.services_detail_images,
                'res_model': self._name,
                'public': True,
                'mimetype': 'image/jpg'
            })
            self.services_images_url = "/web/image/" + str(attachmentid.id)
            self.services_images_attachment_id = attachmentid.id
                
class newswebsitemnc(models.Model):
    _name = 'news.website.mnc'
    _inherit = ['website.seo.metadata', 'website.published.multi.mixin']
    _rec_name = 'news_name'
    _order = 'news_name'
    
    # plan
    news_home_priview = fields.Boolean(default=False, help="Set to priview at home")
    news_name = fields.Char(string="Name News")
    news_description = fields.Text(string="Description News")
    news_images = fields.Binary(string="Images News")
    news_images_fname = fields.Char(string="Images News Name")
    website_id = fields.Many2one('website')
    news_detail = fields.Html(string='News Detail Page')
    
    @api.depends('news_name')
    def _compute_website_url(self):
        super(newswebsitemnc, self)._compute_website_url()
        for news in self:
            if news.id:  # avoid to perform a slug on a not yet saved record in case of an onchange.
                news.website_url = '/berita/%s' % slug(news)
                
                
class ourclientswebsitemnc(models.Model):
    _name = 'ourclients.website.mnc'
    
    ourclients_images_fname = fields.Char(string="Images Ourclients Name")
    ourclients_images = fields.Binary(string="Ourclients Images")
    website_id = fields.Many2one('website')
    
class certificatewebsitemnc(models.Model):
    _name = 'certificate.website.mnc'
    
    certificate_images_fname = fields.Char(string="Images Certificate Name")
    certificate_images = fields.Binary(string="Certificate Images")
    website_id = fields.Many2one('website')
    certificate_desc = fields.Char(string="Certificate Description")
    

class carrierwebsitemnc(models.Model):
    _name = 'carrier.website.mnc'
    _inherit = ['website.seo.metadata', 'website.published.multi.mixin']
    _rec_name = 'carrier_kode'
    _order = 'carrier_kode'
    
    carrier_division = fields.Char(string="Divisi")
    carrier_posisi = fields.Char(string="Posisi")
    carrier_lokasi = fields.Char(string="Lokasi")
    carrier_kode = fields.Char(string="Kode")
    website_id = fields.Many2one('website')
    
    carrier_detail = fields.Html(string='Carrier Detail Page')
    
    
    @api.depends('carrier_kode')
    def _compute_website_url(self):
        super(carrierwebsitemnc, self)._compute_website_url()
        for carrier in self:
            if carrier.id:  # avoid to perform a slug on a not yet saved record in case of an onchange.
                carrier.website_url = '/karir/%s' % slug(carrier)
    
class manajemenwebsitemnc(models.Model):
    _name = 'manajemen.website.mnc'
    
    manajemen_images_fname = fields.Char(string="Manajemen Images Name")
    manajemen_images = fields.Binary(string="Manajemen Images")
    manajemen_title = fields.Char(string="Manajemen Title")
    manajemen_subtitle = fields.Char(string="Manajemen Subtitle")
    manajemen_description = fields.Text(string="Manajemen Description")
    website_id = fields.Many2one('website')
    
class direksiwebsitemnc(models.Model):
    _name = 'direksi.website.mnc'
    
    direksi_images_fname = fields.Char(string="Direksi Images Name")
    direksi_images = fields.Binary(string="Direksi Images")
    direksi_title = fields.Char(string="Direksi Title")
    direksi_subtitle = fields.Char(string="Manajemen Subtitle")
    direksi_description = fields.Text(string="Direksi Description")
    website_id = fields.Many2one('website')
    
    
        
class mobilegaleryhomewebsitemnc(models.Model):
    _name = 'mobilegaleryhome.website.mnc'
    _order = 'sequence'
    
    sequence = fields.Integer(string="Sequence")
    mobilegaleryhome_images_fname = fields.Char(string="Mobile Galery Home Images Name")
    mobilegaleryhome_images = fields.Binary(string="Mobile Galery Home Images")
    mobilegaleryhome_images_url = fields.Char(string="Mobile Galery Images URL")
    mobilegaleryhome_images_attachment_id = fields.Many2one('ir.attachment', string="Mobile Galery Images Attachment ID")
    mobilegaleryhome_title = fields.Char(string="Mobile Galery Home Title")
    mobilegaleryhome_description = fields.Text(string="Mobile Galery Home Description")
    website_id = fields.Many2one('website')

# ===== tambahan dady =====

class awardswebsitemnc(models.Model):
    _name = 'awards.website.mnc'
    _description = 'awards List'
    
    awards_images_fname = fields.Char(string="Images Awards Name")
    awards_images = fields.Binary(string="Awards Images")
    website_id = fields.Many2one('website')   
    
    @api.onchange('mobilegaleryhome_images')
    def onchange_attachments_data(self):
        if self.mobilegaleryhome_images_attachment_id:
            get_attachment_id = self.env['ir.attachment'].search([('id', '=', self.mobilegaleryhome_images_attachment_id.id)])
            get_attachment_id.write({'datas': self.mobilegaleryhome_images,'name': self.mobilegaleryhome_images_fname})
            self.mobilegaleryhome_images_url = "/web/image/" + str(self.mobilegaleryhome_images_attachment_id.id)
        else:
            attachmentid = self.env['ir.attachment'].create({
                'name': self.mobilegaleryhome_images_fname,
                'type': 'binary',
                'datas': self.mobilegaleryhome_images,
                'res_model': self._name,
                'public': True,
                'mimetype': 'image/jpg'
            })
            self.mobilegaleryhome_images_url = "/web/image/" + str(attachmentid.id)
            self.mobilegaleryhome_images_attachment_id = attachmentid.id
            
            
class Website(models.Model):
    _inherit = "website"

    # HOME
    home_images_fname = fields.Char(string="Images Home Name")
    home_images = fields.Binary(string="Images Home")
    home_images_url = fields.Char(string="Home Images URL")
    home_images_attachment_id = fields.Many2one('ir.attachment', string="Home Images Attachment ID")
    # for mobile
    mobilegaleryhome_ids = fields.One2many('mobilegaleryhome.website.mnc', 'website_id', string='Mobile Galery Home')
    
    home_title = fields.Char(string="Title Images Home")
    home_detail = fields.Text(string="Detail Images Home")
    home_map = fields.Text(string="Maps")
    
    home_video_fname = fields.Char(string="Home Video Name")
    home_video = fields.Binary(string="Home Video")
    home_video_url = fields.Char(string="Home Video URL")
    home_video_attachment_id = fields.Many2one('ir.attachment', string="Home Video Attachment ID")
    
    
    certificate_ids = fields.One2many('certificate.website.mnc', 'website_id', string='Certificate')
    awards_ids = fields.One2many('awards.website.mnc', 'website_id', string='Certificate')
    
    # ABOUT US
    aboutus_description = fields.Text(string="Description About Us")
    aboutus_images_fname = fields.Char(string="Images About Us Name")
    aboutus_images = fields.Binary(string="Images About Us")
    
    aboutus_visi = fields.Char(string="About Us Visi Title")
    aboutus_visi_description = fields.Char(string="About Us Visi Description")
    aboutus_misi = fields.Char(string="About Us Misi Title")
    aboutus_misi_description = fields.Char(string="About Us Misi Description")
    aboutus_client = fields.Char(string="About Us Client Title")
    ourclients_ids = fields.One2many('ourclients.website.mnc', 'website_id', string='Ourclients')
    
    aboutus_manajemen_direction_title = fields.Char(string="About Us Manajemen & Direction Title")
    aboutus_komisaris_title = fields.Char(string="About Us Komisaris Title")
    aboutus_direction_title = fields.Char(string="About Us Direction Title")
    manajemen_ids = fields.One2many('manajemen.website.mnc', 'website_id', string='Manajemen')
    direksi_ids = fields.One2many('direksi.website.mnc', 'website_id', string='Direksi')
    
    aboutus_structure_title = fields.Char(string="About Us Structure Title")
    aboutus_structure_image_fname = fields.Char(string="About Us Structure Image Name")
    aboutus_structure_image = fields.Binary(string="About Us Structure Image")
    
    
    aboutus_pdf_download_fname = fields.Char(string="PDF Download Name")
    aboutus_pdf_download = fields.Binary(string="PDF Download Name")
    aboutus_pdf_download_url = fields.Char(string="PDF Download URL")
    aboutus_pdf_download_attachment_id = fields.Many2one('ir.attachment', string="PDF Download Attachment ID")
    
    #SERVICES
    services_ids = fields.One2many('services.website.mnc', 'website_id', string='Services')
    
    #NEWS
    news_ids = fields.One2many('news.website.mnc', 'website_id', string='News')
    
    #CARRIER
    carrier_ids = fields.One2many('carrier.website.mnc', 'website_id', string='Carrier')
    
    
    #CONTACTUS
    contactus_images_fname = fields.Char(string="Images Contact us Name")
    contactus_images = fields.Binary(string="Images Contact us")
    
    # FOOTER
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    phone = fields.Char(string="Footer Call Hunting")
    call_direct = fields.Char(string="Footer Call Direct")
    email = fields.Char(string="Footer Email")
    footer_whatsapp = fields.Char(string="Footer Whatsapp")
    whatsapp = fields.Char(string="Whatsapp")
    text_whatsapp = fields.Text(string="Footer Text Whatsapp")
    whatsapp_url = fields.Char(string="Footer whatsapp URL")
    website_url = fields.Char(string="Footer Website URL")
    
    
    @api.onchange('whatsapp','text_whatsapp')
    def onchange_whatsapp_url(self):
        if self.whatsapp and self.text_whatsapp:
            self.whatsapp_url = "https://api.whatsapp.com/send?phone="+str(self.whatsapp)+"&text="+str(self.text_whatsapp)
    
    
    @api.onchange('home_images')
    def onchange_attachments_data(self):
        if self.home_images_attachment_id:
            get_attachment_id = self.env['ir.attachment'].search([('id', '=', self.home_images_attachment_id.id)])
            get_attachment_id.write({'datas': self.home_images,'name': self.home_images_fname})
        else:
            attachmentid = self.env['ir.attachment'].create({
                'name': self.home_images_fname,
                'type': 'binary',
                'datas': self.home_images,
                'res_model': self._name,
                'public': True,
                'mimetype': 'image/jpg'
            })
            self.home_images_url = "/web/image/" + str(attachmentid.id)
            self.home_images_attachment_id = attachmentid.id

    
    @api.onchange('home_video')
    def onchange_attachments_video_data(self):
        if self.home_video_attachment_id:
            get_attachment_id = self.env['ir.attachment'].search([('id', '=', self.home_video_attachment_id.id)])
            get_attachment_id.write({'datas': self.home_video,'name': self.home_video_fname})
        else:
            attachmentid = self.env['ir.attachment'].create({
                'name': self.home_video_fname,
                'type': 'binary',
                'datas': self.home_video,
                'res_model': self._name,
                'public': True,
                'mimetype': 'image/jpg'
            })
            self.home_video_url = "/web/image/" + str(attachmentid.id)
            self.home_video_attachment_id = attachmentid.id
    
    @api.onchange('aboutus_pdf_download')
    def onchange_aboutus_pdf_download(self):
        if self.aboutus_pdf_download_attachment_id:
            get_attachment_id = self.env['ir.attachment'].search([('id', '=', self.aboutus_pdf_download_attachment_id.id)])
            get_attachment_id.write({'datas': self.aboutus_pdf_download,'name': self.aboutus_pdf_download_fname})
        else:
            attachmentid = self.env['ir.attachment'].create({
                'name': self.aboutus_pdf_download_fname,
                'type': 'binary',
                'datas': self.aboutus_pdf_download,
                'res_model': self._name,
                'public': True,
                'mimetype': 'image/jpg'
            })
            self.aboutus_pdf_download_url = "/web/image/" + str(attachmentid.id)
            self.aboutus_pdf_download_attachment_id = attachmentid.id