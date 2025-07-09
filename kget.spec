#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Versatile and user-friendly download manager for KDE4
Name:		kget
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kget/-/archive/%{gitbranch}/kget-%{gitbranchd}.tar.bz2#/kget-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{ftpdir}/release-service/%{version}/src/kget-%{version}.tar.xz
%endif
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	pkgconfig(libmms)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KTorrent6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(LibKWorkspace) < 6.27.60
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qtbase-sql-postgresql
BuildRequires:	qt6-qtbase-sql-odbc
BuildRequires:	qt6-qtbase-sql-mariadb
BuildRequires:	qt6-qtbase-sql-firebird
BuildRequires:	plasma6-xdg-desktop-portal-kde

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
%{_datadir}/qlogging-categories6/kget.categories
%{_bindir}/kget
%{_datadir}/config.kcfg/kget*.kcfg
%{_datadir}/metainfo/org.kde.kget.appdata.xml
%{_datadir}/dbus-1/services/org.kde.kget.service
%{_datadir}/icons/hicolor/*/*/*
%dir %{_libdir}/qt6/plugins/kget
%{_libdir}/qt6/plugins/kget/kget_bittorrent.so
%{_libdir}/qt6/plugins/kget/kget_checksumsearchfactory.so
%{_libdir}/qt6/plugins/kget/kget_kio.so
%{_libdir}/qt6/plugins/kget/kget_metalinkfactory.so
%{_libdir}/qt6/plugins/kget/kget_mirrorsearchfactory.so
%{_libdir}/qt6/plugins/kget/kget_mmsfactory.so
%{_libdir}/qt6/plugins/kget/kget_multisegkiofactory.so
%dir %{_libdir}/qt6/plugins/kget_kcms
%{_libdir}/qt6/plugins/kget_kcms/kcm_kget_bittorrentfactory.so
%{_libdir}/qt6/plugins/kget_kcms/kcm_kget_checksumsearchfactory.so
%{_libdir}/qt6/plugins/kget_kcms/kcm_kget_metalinkfactory.so
%{_libdir}/qt6/plugins/kget_kcms/kcm_kget_mirrorsearchfactory.so
%{_libdir}/qt6/plugins/kget_kcms/kcm_kget_mmsfactory.so
%{_libdir}/qt6/plugins/kget_kcms/kcm_kget_multisegkiofactory.so
%{_datadir}/applications/org.kde.kget.desktop
%{_datadir}/kget/pics/kget_splash.png
%{_datadir}/knotifications6/kget.notifyrc
%{_datadir}/kio/servicemenus/kget_download.desktop
%{_libdir}/libkgetcore.so*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kget-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build

# We don't need it because there are no headers anyway
rm -f %{buildroot}%{_kde6_libdir}/libkgetcore.so

%find_lang %{name} --all-name --with-html --with-man
