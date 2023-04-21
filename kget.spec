Summary:	Versatile and user-friendly download manager for KDE4
Name:		kget
Version:	23.04.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	libktorrent-devel
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Torrent)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(Qca-qt5)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(LibKWorkspace)
Conflicts:	kdenetwork4-devel < 3:4.11.0
Obsoletes:	%{name} < 3:19.04.0-3

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
%{_datadir}/qlogging-categories5/kget.categories
%{_bindir}/kget
%{_datadir}/config.kcfg/kget*.kcfg
%{_datadir}/metainfo/org.kde.kget.appdata.xml
%{_datadir}/dbus-1/services/org.kde.kget.service
%{_datadir}/icons/hicolor/*/*/*
%dir %{_libdir}/qt5/plugins/kget
%{_libdir}/qt5/plugins/kget/kget_bittorrent.so
%{_libdir}/qt5/plugins/kget/kget_checksumsearchfactory.so
%{_libdir}/qt5/plugins/kget/kget_kio.so
%{_libdir}/qt5/plugins/kget/kget_metalinkfactory.so
%{_libdir}/qt5/plugins/kget/kget_mirrorsearchfactory.so
%{_libdir}/qt5/plugins/kget/kget_mmsfactory.so
%{_libdir}/qt5/plugins/kget/kget_multisegkiofactory.so
%dir %{_libdir}/qt5/plugins/kget_kcms
%{_libdir}/qt5/plugins/kget_kcms/kcm_kget_bittorrentfactory.so
%{_libdir}/qt5/plugins/kget_kcms/kcm_kget_checksumsearchfactory.so
%{_libdir}/qt5/plugins/kget_kcms/kcm_kget_metalinkfactory.so
%{_libdir}/qt5/plugins/kget_kcms/kcm_kget_mirrorsearchfactory.so
%{_libdir}/qt5/plugins/kget_kcms/kcm_kget_mmsfactory.so
%{_libdir}/qt5/plugins/kget_kcms/kcm_kget_multisegkiofactory.so
%{_datadir}/applications/org.kde.kget.desktop
%{_datadir}/kget/pics/kget_splash.png
%{_datadir}/knotifications5/kget.notifyrc
%{_datadir}/kservicetypes5/kget_plugin.desktop
%{_datadir}/kxmlgui5/kget/kgetui.rc
%{_datadir}/kio/servicemenus/kget_download.desktop

#----------------------------------------------------------------------------

%define kgetcore_major 5
%define libkgetcore %mklibname kgetcore %{kgetcore_major}

%package -n %{libkgetcore}
Summary:	Shared library for KGet
Group:		System/Libraries
Obsoletes:	%{mklibname kgetcore 5} < 3:19.04.0-3

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
