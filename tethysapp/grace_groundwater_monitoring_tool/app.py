from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting, CustomSetting


class GraceGroundwaterMonitoringTool(TethysAppBase):
    """
    Tethys app class for GRACE Groundwater Monitoring Tool.
    """

    name = 'GRACE Groundwater Monitoring Tool'
    index = 'grace_groundwater_monitoring_tool:home'
    icon = 'grace_groundwater_monitoring_tool/images/logo.jpg'
    package = 'grace_groundwater_monitoring_tool'
    root_url = 'grace-groundwater-monitoring-tool'
    color = '#222222'
    description = 'This app displays data collected from NASAs GRACE and GRACE-FO missions.  It also displays soil moisture and surface water data from NOAAs GLDAS model and it displays changes in groundwater data derived from the above mentioned datasets.'
    tags = 'Hydrology,Groundwater,GRACE,GRACE-FO,GLDAS'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='grace-groundwater-monitoring-tool',
                controller='grace_groundwater_monitoring_tool.controllers.home'
            ),
            UrlMap(
                name='global-map',
                url='global-map',
                controller='grace_groundwater_monitoring_tool.controllers.global_map'
            ),
            UrlMap(
                name='check-for-updates',
                url='grace-groundwater-monitoring-tool/check-for-updates',
                controller='grace_groundwater_monitoring_tool.ajax_controllers.check_for_updates'
            ),
            UrlMap(
                name='download-hs-files',
                url='grace-groundwater-monitoring-tool/download-hs-files',
                controller='grace_groundwater_monitoring_tool.ajax_controllers.download_hs_files'
            ),
            UrlMap(
                name='update-global-files',
                url='grace-groundwater-monitoring-tool/update-global-files',
                controller='grace_groundwater_monitoring_tool.controllers.update_global_files'
            ),
            UrlMap(
                name='region',
                url='region',
                controller='grace_groundwater_monitoring_tool.controllers.region'
            ),
            UrlMap(
                name='add-region',
                url='add-region',
                controller='grace_groundwater_monitoring_tool.controllers.add_region'
            ),
            UrlMap(
                name='get-plot-global',
                url='global-map/get-plot-global',
                controller='grace_groundwater_monitoring_tool.ajax_controllers.get_plot_global'
            ),
            UrlMap(
                name='get-plot-reg-pt',
                url='region/get-plot-reg-pt',
                controller='grace_groundwater_monitoring_tool.ajax_controllers.get_plot_reg_pt'
            ),




            UrlMap(name='add-region-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/submit',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.region_add'
            ),
            UrlMap(name='initial-processing-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/initial',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_initial_processing'
            ),
            UrlMap(name='jpl-tot-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/jpl-tot',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_jpl_tot'
            ),
            UrlMap(name='jpl-gw-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/jpl-gw',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_jpl_gw'
            ),
            UrlMap(name='csr-tot-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/csr-tot',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_csr_tot'
            ),
            UrlMap(name='csr-gw-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/csr-gw',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_csr_gw'
            ),
            UrlMap(name='gfz-tot-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/gfz-tot',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_gfz_tot'
            ),
            UrlMap(name='gfz-gw-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/gfz-gw',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_gfz_gw'
            ),
            UrlMap(name='avg-tot-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/avg-tot',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_avg_tot'
            ),
            UrlMap(name='avg-gw-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/avg-gw',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_avg_gw'
            ),
            UrlMap(name='sw-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/sw',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_sw'
            ),
            UrlMap(name='soil-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/soil',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_soil'
            ),
            UrlMap(name='cleanup-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/cleanup',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_cleanup'
            ),
            UrlMap(name='update-ajax',
                   url='grace-groundwater-monitoring-tool/add-region/update',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.subset_update'
            ),



            UrlMap(
                name='add-thredds-server',
                url='add-thredds-server',
                controller='grace_groundwater_monitoring_tool.controllers.add_thredds_server'
            ),
            UrlMap(name='add-thredds-server-ajax',
                   url='grace-groundwater-monitoring-tool/add-thredds-server/submit',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.thredds_server_add'
            ),
            UrlMap(name='update-thredds-servers-ajax',
                   url='grace-groundwater-monitoring-tool/manage-thredds-servers/submit',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.thredds_server_update'
            ),
            UrlMap(name='delete-thredds-server-ajax',
                   url='grace-groundwater-monitoring-tool/manage-thredds-servers/delete',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.thredds_server_delete'
            ),
            UrlMap(
                name='manage-regions',
                url='manage-regions',
                controller='grace_groundwater_monitoring_tool.controllers.manage_regions'
            ),
            UrlMap(name='manage-regions-table',
                   url='grace-groundwater-monitoring-tool/manage-regions/table',
                   controller='grace_groundwater_monitoring_tool.controllers.manage_regions_table'
            ),
            UrlMap(name='delete-regions-ajax',
                   url='grace-groundwater-monitoring-tool/manage-regions/delete',
                   controller='grace_groundwater_monitoring_tool.ajax_controllers.region_delete'
            ),
            UrlMap(
                name='manage-thredds-servers',
                url='manage-thredds-servers',
                controller='grace_groundwater_monitoring_tool.controllers.manage_thredds_servers'
            ),
            UrlMap(name='manage-thredds-servers-table',
                   url='grace-groundwater-monitoring-tool/manage-thredds-servers/table',
                   controller='grace_groundwater_monitoring_tool.controllers.manage_thredds_servers_table'
            ),
            UrlMap(name='api_get_point_values',
                   url='grace-groundwater-monitoring-tool/api/GetPointValues',
                   controller='grace_groundwater_monitoring_tool.api.api_get_point_values'),

        )

        return url_maps

    def custom_settings(self):
        custom_settings = (
            CustomSetting(
                name='Local Thredds Folder Path',
                type=CustomSetting.TYPE_STRING,
                description='Path to Global NetCDF Directory (Local Folder Mounted to Thredds Docker)',
                required=True,
            ),
            CustomSetting(
                name='Thredds wms URL',
                type=CustomSetting.TYPE_STRING,
                description='URL to thredds Global Directory folder.  Should end in .../thredds/ (ex: 127.0.0.1:7000/thredds/)',
                required=True,
            ),
        )
        return custom_settings

    def persistent_store_settings(self):

        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='grace_db',
                description='For storing Region and Thredds metadata',
                required=True,
                initializer='grace_groundwater_monitoring_tool.model.init_grace_db',
                spatial=False,
            ),
        )

        return ps_settings
