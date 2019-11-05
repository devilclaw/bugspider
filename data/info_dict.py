# coding:utf-8
# Merge 2019.4.3
import sys
sys.dont_write_bytecode = True

# keyword
ROBOTS_KEYWORD = 'User-agent'
GIT_KEYWORD = 'repositoryformatversion'
SVN_KEYWORD = 'svn://'
IISPARSE_KEYWORD = 'User-agent'
WORKSPACE_KEYWORD = '<?xml version='
TOMCATXML_KEYWORD = '<web-app'
PHPINFO_KEYWORD='PHP Extension'
ANTSOWOD_STATUSCODE='408'
PHPMYADMIN_KEYWORD = 'Documentation.html'
PHPMYADMIN_LOGIN_OK_KWD = 'mainFrameset'
JQUERY_KEYWORD = '{"files":['
UEDITOR_KEYWORD = '{"state":"'
REDIS_UNAUTH_KEYWORD = 'redis_version'
REDIS_AUTH_KEYWORD = 'Authentication'
DZ_TOOLS_KEYWORD = 'toolpassword'
WEBXML_KEYWORD = '<web-app'
SITESERVER_KEYWORD = 'www.siteserver.cn'
SITESERVER_KEYWORD1 = 'www.bairongsoft.com'
UEDITOR_KEYWORD_OLD = 'fileNameFormat'
UEDITOR_KEYWORD_OLD_STATE = 'state'


# bakfile suffix Format dict
BakFileSuffixFormat = ['.rar', '.zip', '.gz', '.sql.gz', '.tar.gz', '.sql',
                       '.7z', '.backup.rar', '.backup.zip', '.backup.sql',
                       '.backup.tar.gz']

PHPMYADMIN_PASSWORD_DICT = ['', 'root', '123456', 'root123456', 'password',
                            'admin',
                            '1234567', 'huweishen.com', '123qwe']

# mysql password dict
MYSQL_PASSWORD_DICT = ['', 'root', '123456', 'root123456', 'password', 'admin',
                       '123123', 'P@ssw0rd!!', '1234567'
                                               'qwe123', '12345678', 'test',
                       '123qwe!@#', '123456789',
                       '123321', '1314520', '666666', 'woaini', 'fuckyou',
                       '000000',
                       '1234567890', '8888888', 'qwerty', '1qaz2wsx', 'abc123',
                       'abc123456', '1q2w3e4r', '123qwe', '159357', 'p@ssw0rd',
                       'p@55w0rd', 'password!', 'p@ssw0rd!', 'password1',
                       'r00t']

# mssql password dict
MSSQL_PASSWORD_DICT = ['', 'sa', 'root', '123456', 'password', 'admin',
                       '123123', 'P@ssw0rd!!',
                       'qwe123', '12345678', 'test', '123qwe!@#', '123456789',
                       '123321', '1314520', '666666', 'woaini', 'fuckyou',
                       '000000',
                       '1234567890', '8888888', 'qwerty', '1qaz2wsx', 'abc123',
                       'abc123456', '1q2w3e4r', '123qwe', '159357', 'p@ssw0rd',
                       'p@55w0rd', 'password!', 'p@ssw0rd!', 'password1',
                       'sa123456']

# Discuz tools.php dict
DZ_TOOLS_DICT = ['tools.php', 'tools/tools.php', 'ucenter/tools.php',
                 'uc_server/tools.php', 'source/plugin/tools/tools.php',
                 'uc/tools.php', 'uc_server/tools/tools.php']

# phpmyadmin dict
PHPMYADMIN_DICT = ['phpMyAdmin', 'phpMyAdmins', 'phpmyadmin-utf8',
                   'admin/phpmyadmin',
                   'phpMyAdmin0', 'phpMyAdmin1', 'phpMyAdmin2', 'phpMyAdmin_0',
                   'phpMyAdmin_1', 'phpMyAdmin_2', 'phpMyAdmin-0',
                   'phpMyAdmin-1', 'p',
                   'phpMyAdmin-2', 'pma', 'pm_Admin', 'pmd']

# phpinfo dict
PHPINFO_DICT = ['phpinfo.php', 'ceshi.php', 'info.php', 'phpversion.php',
                'a.php', 'test1.php', 'test.php', 'test2.php', 'phpinfo1.php',
                'info1.php', 'x.php', 'xx.php', 'xxx.php', 'tz.php', 'env.php',
                'p.php', 'aspcheck.asp', 'pi.php', 'i.php', 'l.php', '1.php',
                'php.php', 'pi.php', 'tz/tz.php', 'tst.php', 'php_info.php',
                'test1.php']

# bakfile name
#BAKFILE_NAME = ['web', 'www', 'web.config', 'data', 'faisunzip', 'flashfxp',]
BAKFILE_NAME = ['admin', 'backup', 'bbs', 'data', 'faisunzip', 'flashfxp',
                'ftp', 'web', 'www', 'wwwroot.sql', 'sql', 'htdocs',
                'cms', 'public_html', '111', '123', '1', 'jianzhanmoban',
                '新建文件夹', 'db', 'pay', 'm', 'themes','bf','ym', 'test', 'w',
                'bin', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'x', 'y', 'z','0', '2', '3', '4', '5', '6', 
                '7', '8', '9'
                ]

# balfile format
BAKFILE_FORMAT = ['.rar', '.zip', '.tar.gz', '.tar', '.7z']

# bakfile dict
BAKFILE_DICT = ['__zep__/js.zip']
for bakname in BAKFILE_NAME:
    for bakformat in BAKFILE_FORMAT:
        if bakname+bakformat not in BAKFILE_DICT:
            BAKFILE_DICT.append(bakname+bakformat)
#print BAKFILE_DICT
# jquery dict
JQUERY_DICT = ['jQuery-File-Upload/server/php/index.php',
               'jQuery/server/php/index.php',
               'Account/SystemMangment/thirdparty/plugins/jQuery-File-Upload/server/php/index.php',
               'admin/third-part/plugins/jQuery-File-Upload/server/php/index.php',
               'admin/assets/global/plugins/jQuery-File-Upload/server/php/index.php',
               'admin/plugins/jQuery-File-Upload/server/php/index.php',
               'Agent/plugins/jQuery-File-Upload/server/php/index.php',
               'Areas/Admin/Content/plugins/jQuery-File-Upload/server/php/index.php',
               'Areas/Admin/PlugIn/plugins/jQuery-File-Upload/server/php/index.php',
               'chajian/plugins/jQuery-File-Upload/server/php/index.php',
               'Content/js/plugins/jQuery-File-Upload/server/php/index.php',
               'Content/plugins/jQuery-File-Upload/server/php/index.php',
               'js/plugins/jQuery-File-Upload/server/php/index.php',
               'OA/JScript/plugins/jQuery-File-Upload/server/php/index.php',
               'plugins/jQuery-File-Upload/server/php/index.php',
               'Plugin/plugins/jQuery-File-Upload/server/php/index.php',
               'Script/plugins/jQuery-File-Upload/server/php/index.php',
               'Themes/plugins/jQuery-File-Upload/server/php/index.php',
               'Company/plugins/jQuery-File-Upload/server/php/index.php',
               'manager/plugins/jQuery-File-Upload/server/php/index.php',
               'manage/plugins/jQuery-File-Upload/server/php/index.php',
               'layer/plugins/jQuery-File-Upload/server/php/index.php',
               'en/plugins/jQuery-File-Upload/server/php/index.php',
               'Common/plugins/jQuery-File-Upload/server/php/index.php',
               'Administration/Content/plugins/jQuery-File-Upload/server/php/index.php',
               'mgr/plugins/jQuery-File-Upload/server/php/index.php',
               'Components/plugins/jQuery-File-Upload/server/php/index.php',
               'scripts/plugins/jQuery-File-Upload/server/php/index.php',
               'main/plugins/jQuery-File-Upload/server/php/index.php',
               'static/plugins/jQuery-File-Upload/server/php/index.php',
               'assets/global/plugins/jQuery-File-Upload/server/php/index.php',
               'Assets/js/plugins/jQuery-File-Upload/server/php/index.php',
               'assets/plugins/jQuery-File-Upload/server/php/index.php', ]

# ueditor dict
UEDITOR_DICT = ['ueditor/net/controller.ashx?action=',
                'inc/ueditor/net/controller.ashx?action=',
                'incs/ueditor/net/controller.ashx?action=',
                'ueditor1432/net/controller.ashx?action=',
                'ueditor1433/net/controller.ashx?action=',
                'utf8-net/net/controller.ashx?action=',
                'Content/utf8-net/net/controller.ashx?action=',
                'WebEditor/net/controller.ashx?action=',
                'ueditor1_3_5-utf8-net/net/controller.ashx?action=',
                'editor/net/controller.ashx?action=',
                'net/controller.ashx?action=',
                'ashx/controller.ashx?action=',
                'controller.ashx?action=',
                'editor/controller.ashx?action=',
                'ueditor/controller.ashx?action=',
                'Account/SystemMangment/thirdparty/ueditor/net/controller.ashx?action=',
                'admin/third-part/ueditor/net/controller.ashx?action=',
                'admin/ueditor/net/controller.ashx?action=',
                'admin/ueditor/ueditor/net/controller.ashx?action=',
                'Admin/Scripts/ueditor/net/controller.ashx?action=',
                'Agent/ueditor/net/controller.ashx?action=',
                'Areas/Admin/Content/ueditor/net/controller.ashx?action=',
                'Areas/Admin/PlugIn/Ueditor/net/controller.ashx?action=',
                'Areas/PortalsWeb/Ueditor/Net/controller.ashx?action=',
                'chajian/ueditor/net/controller.ashx?action=',
                'Content/js/plugins/ueditor/net/controller.ashx?action=',
                'Editor/UEditor/net/controller.ashx?action=',
                'js/plugins/ueditor/net/controller.ashx?action=',
                'OA/JScript/ueditor/net/controller.ashx?action=',
                'plugins/ueditor/net/controller.ashx?action=',
                'Plugin/ueditor/net/controller.ashx?action=',
                'login/ueditor/net/controller.ashx?action=',
                'config/ueditor/net/controller.ashx?action=',
                'PlugIn/TextEditor/ueditor/net/controller.ashx?action=',
                'Script/UeDitor/net/controller.ashx?action=',
                'Themes/ueditor/net/controller.ashx?action=',
                'Content/ueditor/net/controller.ashx?action=',
                'Company/ueditor/net/controller.ashx?action=',
                'assets/global/plugins/UEditor/net/controller.ashx?action=',
                'manager/ueditor/net/controller.ashx?action=',
                'manage/ueditor/net/controller.ashx?action=',
                'mager/ueditor/net/controller.ashx?action=',
                'layer/ueditor/net/controller.ashx?action=',
                'JS/ueditor/net/controller.ashx?action=',
                'en/ueditor/net/controller.ashx?action=',
                'Assets/js/ueditor/net/controller.ashx?action=',
                'Common/ueditor/net/controller.ashx?action=',
                'Administration/Content/UEditor/net/controller.ashx?action=',
                'mgr/ueditor/net/controller.ashx?action=',
                'Components/ueditor/net/controller.ashx?action=',
                'scripts/ueditor/net/controller.ashx?action=',
                'scripts/ueditor1_4_3/net/controller.ashx?action=',
                'main/ueditor/net/controller.ashx?action=',
                'Admin/UEditor/ueditor/net/controller.ashx?action=',
                'static/Ueditor/net/controller.ashx?action=',
                'ue/net/controller.ashx?action=',
                'Controls/ueditor/net/controller.ashx?action=',
                'login/ueditor/net/controller.ashx?action=',
                'comm/ueditor/net/controller.ashx?action=',
                'BDEditor/net/controller.ashx?action=']

UEDITOR_DICT_OLD = ['ueditor/',
                'inc/ueditor/',
                'incs/ueditor/',
                'ueditor1432/',
                'ueditor1433/',
                'utf8-net/',
                'Content/utf8-net/',
                'WebEditor/',
                'ueditor136/',
                'ueditor1_3_6-utf8-net/',
                'ueditor1_3_5-utf8-net/',
                'editor/',
                'ue/',
                '',
                'ashx/',
                'editor/',
                'ueditor1/',
                'ueditor2/',
                'ueditor3/',
                'Account/SystemMangment/thirdparty/ueditor/',
                'admin/third-part/ueditor/',
                'admin/ueditor/',
                'admin/ueditor/ueditor/',
                'Admin/Scripts/ueditor/',
                'Agent/ueditor/',
                'Areas/Admin/Content/ueditor/',
                'Areas/Admin/PlugIn/Ueditor/',
                'Areas/PortalsWeb/Ueditor/',
                'chajian/ueditor/',
                'Content/js/plugins/ueditor/',
                'Editor/UEditor/',
                'js/plugins/ueditor/',
                'OA/JScript/ueditor/',
                'plugins/ueditor/',
                'Plugin/ueditor/',
                'login/ueditor/',
                'config/ueditor/',
                'PlugIn/TextEditor/ueditor/',
                'Script/UeDitor/',
                'Themes/ueditor/',
                'Content/ueditor/',
                'Company/ueditor/',
                'assets/global/plugins/UEditor/',
                'manager/ueditor/',
                'manage/ueditor/',
                'mager/ueditor/',
                'layer/ueditor/',
                'JS/ueditor/',
                'en/ueditor/',
                'Assets/js/ueditor/',
                'Common/ueditor/',
                'Administration/Content/UEditor/',
                'mgr/ueditor/',
                'Components/ueditor/',
                'scripts/ueditor/',
                'scripts/ueditor1_4_3/',
                'main/ueditor/',
                'Admin/UEditor/ueditor/',
                'static/Ueditor/',
                'Controls/ueditor/',
                'login/ueditor/',
                'comm/ueditor/',
                'BDEditor/']

PASSWORD_DIC = ['redis', 'password', 'foobared', 'root', 'admin', '123456',
                '188281MWWxjk', 'discuz', 'admin12345678', 'admin123456789',
                'aa123456789', 'zxcvbnm', 'admin123', 'manager', 'asdfghjkl',
                'wang123456', '123456789qq', '1234554321', '7894561230',
                '123456789', 'admin8', '1qw23er4', 'admin888', 'asd123',
                '789456123', 'a123654', 'qwe123', '000000000', '123698745',
                '1q2w3e4r', '123123', 'w123456', '1233211234567',
                '7708801314520', '741852963', '147258369', 'kunlun', 'zxc123',
                'qwertyuiop', '123456789..', '1q2w3e', '123abc', 'qaz123456',
                '123456asd', 'qwe123a', '123456a', 'zxcvbnm123', 'qazwsxedc',
                '0123456789', '1314520520', 'q123456789', '123456789a',
                'caonima', 'admin123456', 'z123456789', 'abcd123', 'woaini1314',
                '123456789', '1234567', 'qwe123456', '5841314520', '666666',
                'aa123456', '1234567899', '5201314', '1234567891', '1234567890',
                '123456abc', 'iloveyou', 'admin1234', 'abc123', '123456789.',
                'admin999', '1111111111', '654321', 'aaa123456', 'q123456',
                '0000000000000000', 'www123456', 'woaini123', '12345678910',
                '0000000000', 'asd123456', 'abc123456', 'zxc123456',
                'qq5201314', 'a12345678', 'qq123456', '123456.',
                '1111111111111111', '52013145201314', '12345678', '12345678900',
                '123123123', 'abc123456789', '123456q', 'woaini1314520',
                'abcd123456', 'qq123456789', '000000', 'a5201314', 'admin456',
                'abcd1234', '1357924680', '123456aa', 'qwerty', 'zhang123456',
                'woaini', '5201314520', '111111111', 'as123456', '1472583690',
                'z123456', 'phpcms', '123456789abc', '888888', '9876543210',
                'admin!@#', '112233', '987654321', '123456qq', '123456..',
                'ABC@123', '135792468', 'w123456789', 'a123456789', 'woaini521',
                'woaini520', 'aini1314', 'q1w2e3r4', '111111', '123456789q',
                '110120119', 'a123123', 'abc@123', 'a123456']
