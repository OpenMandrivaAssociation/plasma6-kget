Summary:	Versatile and user-friendly download manager for KDE4
Name:		kget
Version:	17.04.0
Release:	1
Epoch:		3
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
BuildRequires:	kde-baseapps-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libktorrent-devel
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(sqlite3)
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

%files
%doc %{_kde_docdir}/HTML/*/kget
%{_kde_bindir}/kget
%{_kde_applicationsdir}/kget.desktop
%{_kde_appsdir}/kget
%{_kde_appsdir}/kconf_update/kget*
%{_kde_appsdir}/dolphinpart/kpartplugins/kget_plug_in.rc
%{_kde_appsdir}/dolphinpart/kpartplugins/kget_plug_in.desktop
%{_kde_appsdir}/khtml/kpartplugins/kget_plug_in.rc
%{_kde_appsdir}/khtml/kpartplugins/kget_plug_in.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/kget_plug_in.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/kget_plug_in.rc
%{_kde_services}/kget_*
%{_kde_services}/plasma-engine-kget.desktop
%{_kde_services}/kgetbarapplet-default.desktop
%{_kde_services}/kgetpiechartapplet-default.desktop
%{_kde_services}/plasma-runner-kget.desktop
%{_kde_services}/ServiceMenus/kget_download.desktop
%{_kde_servicetypes}/kget_*
%{_kde_libdir}/kde4/krunner_kget.so
%{_kde_libdir}/kde4/kget_*
%{_kde_libdir}/kde4/plasma_engine_kget.so
%{_kde_libdir}/kde4/kcm_kget_checksumsearchfactory.so
%{_kde_libdir}/kde4/kcm_kget_metalinkfactory.so
%{_kde_libdir}/kde4/kcm_kget_mirrorsearchfactory.so
%{_kde_libdir}/kde4/kcm_kget_mmsfactory.so
%{_kde_libdir}/kde4/kcm_kget_multisegkiofactory.so
%{_kde_libdir}/kde4/plasma_kget_barapplet.so
%{_kde_libdir}/kde4/plasma_kget_piechart.so
%{_kde_datadir}/config.kcfg/kget*
%{_kde_iconsdir}/*/*/apps/kget.*

#----------------------------------------------------------------------------

%define kgetcore_major 4
%define libkgetcore %mklibname kgetcore %{kgetcore_major}

%package -n %{libkgetcore}
Summary:	Shared library for KGet
Group:		System/Libraries

%description -n %{libkgetcore}
Shared library for KGet.

%files -n %{libkgetcore}
%{_kde_libdir}/libkgetcore.so.%{kgetcore_major}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

# We don't need it because there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libkgetcore.so
