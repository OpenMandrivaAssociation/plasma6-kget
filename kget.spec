Summary:	Versatile and user-friendly download manager for KDE4
Name:		kget
Version:	18.12.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	libktorrent-devel
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	cmake(KF5Completion) cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5I18n) 
BuildRequires:	cmake(KF5IconThemes) cmake(KF5KDELibs4Support) cmake(KF5KIO) cmake(KF5Notifications) cmake(KF5Service) 
BuildRequires:	cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5DBus) cmake(Qt5Gui) cmake(Qt5Network) cmake(Qt5Sql) 
BuildRequires:	cmake(Qt5Widgets) cmake(Qt5Xml) cmake(Gpgmepp) cmake(Qca-qt5) cmake(QGpgme) cmake(ECM) cmake(Qt5Test) cmake ninja
BuildRequires:	cmake(KF5KCMUtils) cmake(KF5NotifyConfig) cmake(KF5Wallet)
Conflicts:	kdenetwork4-devel < 3:4.11.0

%description
KGet is a versatile and user-friendly download manager.
Features:
- Downloading files from FTP and HTTP(S) sources.
- Pausing and resuming of downloading files, as well as the ability
  to restart   a download.
- Tells lots of information about current and pending downloads.
- Embedding into system tray.
- Integration with the Konqueror web browser.
- Metalink support which contains multiple URLs for downloads, along
  with checksums and other information.

%files -f %{name}.lang
%{_sysconfdir}/xdg/kget.categories
%{_bindir}/kget
%{_datadir}/config.kcfg/kget*.kcfg
%{_datadir}/metainfo/org.kde.kget.appdata.xml
%{_datadir}/dbus-1/services/org.kde.kget.service
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/qt5/plugins/kcm_kget_bittorrentfactory.so
%{_libdir}/qt5/plugins/kcm_kget_checksumsearchfactory.so
%{_libdir}/qt5/plugins/kcm_kget_metalinkfactory.so
%{_libdir}/qt5/plugins/kcm_kget_mirrorsearchfactory.so
%{_libdir}/qt5/plugins/kcm_kget_mmsfactory.so
%{_libdir}/qt5/plugins/kcm_kget_multisegkiofactory.so
%{_libdir}/qt5/plugins/kget/kget_bittorrent.so
%{_libdir}/qt5/plugins/kget/kget_checksumsearchfactory.so
%{_libdir}/qt5/plugins/kget/kget_kio.so
%{_libdir}/qt5/plugins/kget/kget_metalinkfactory.so
%{_libdir}/qt5/plugins/kget/kget_mirrorsearchfactory.so
%{_libdir}/qt5/plugins/kget/kget_mmsfactory.so
%{_libdir}/qt5/plugins/kget/kget_multisegkiofactory.so
%{_libdir}/qt5/plugins/kget_browser_integration.so
%{_datadir}/applications/org.kde.kget.desktop
%{_datadir}/dolphinpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/dolphinpart/kpartplugins/kget_plug_in.rc
%{_datadir}/kconf_update/kget.upd
%{_datadir}/kconf_update/kget_limitdownloads.pl
%{_datadir}/kconf_update/kget_sensitive.pl
%{_datadir}/kget/pics/kget_splash.png
%{_datadir}/khtml/kpartplugins/kget_plug_in.desktop
%{_datadir}/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/knotifications5/kget.notifyrc
%{_datadir}/kservices5/ServiceMenus/kget_download.desktop
%{_datadir}/kservices5/kget_bittorrentfactory_config.desktop
%{_datadir}/kservices5/kget_checksumsearchfactory_config.desktop
%{_datadir}/kservices5/kget_metalinkfactory_config.desktop
%{_datadir}/kservices5/kget_mirrorsearchfactory_config.desktop
%{_datadir}/kservices5/kget_mmsfactory_config.desktop
%{_datadir}/kservices5/kget_multisegkiofactory_config.desktop
%{_datadir}/kservicetypes5/kget_plugin.desktop
%{_datadir}/kwebkitpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/kwebkitpart/kpartplugins/kget_plug_in.rc
%{_datadir}/kxmlgui5/kget/kgetui.rc

#----------------------------------------------------------------------------

%define kgetcore_major 5
%define libkgetcore %mklibname kgetcore %{kgetcore_major}

%package -n %{libkgetcore}
Summary:	Shared library for KGet
Group:		System/Libraries

%description -n %{libkgetcore}
Shared library for KGet.

%files -n %{libkgetcore}
%{_kde5_libdir}/libkgetcore.so.%{kgetcore_major}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

# We don't need it because there are no headers anyway
rm -f %{buildroot}%{_kde5_libdir}/libkgetcore.so

%find_lang %{name} --all-name --with-html --with-man
