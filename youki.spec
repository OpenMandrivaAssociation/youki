Summary: Fast media player
Name: youki
Version: 0.05.2
Release: %mkrel 2
License: GPLv2+
Group: Sound
Source0: http://redmine.youki.mp/attachments/download/25/%{name}_%{version}-1mpx1.tar.gz
Patch0: youki_0.05.2-link.patch
Patch1: youki_0.05.2-gcc44.patch
Patch2: youki_0.05.2-str-fmt.patch
Patch3: youki_0.05.2-module-link.patch
URL: http://youki.mp/
BuildRequires: pygtk2.0-devel
BuildRequires: boost-devel
BuildRequires: dbus-c++-devel
BuildRequires: dbus-glib-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: hal-devel
BuildRequires: taglib-gio-devel
BuildRequires: libofa-devel
BuildRequires: sigx-devel
BuildRequires: xerces-c28-devel
BuildRequires: gettext-devel
BuildRequires: libglademm2.4-devel
BuildRequires: sqlite3-devel
BuildRequires: libsoup-2.4-devel
BuildRequires: curl-devel
BuildRequires: startup-notification-devel
BuildRequires: fam-devel
BuildRequires: libalsa-devel
BuildRequires: cdda-devel
BuildRequires: zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Youki is a very simple, powerful and very fast media player.

#-----------------------------------------------------------------------
%define major 0
%define libname %mklibname mpx %major

%package -n %libname
Summary: Shared libraries for %name
Group: System/Libraries

%description -n %libname
This package contains shared libraries for youki.

#-----------------------------------------------------------------------
%define halcc_api 1.0
%define halcc_major 3
%define libhalcc %mklibname halcc %halcc_api %halcc_major

%package -n %libhalcc
Summary: Shared libraries for %name
Group: System/Libraries

%description -n %libhalcc
This package contains shared libraries for youki.

#-----------------------------------------------------------------------
%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %libname = %version
Requires: %libhalcc = %version

%description devel
This package contains development files for youki.

#-----------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0 -b .link
%patch1 -p0 -b .gcc
%patch2 -p0 -b .str
%patch3 -p0 -b .module

sed -i -e 's#ac_boost_path/lib#ac_boost_path/%{_lib}#' -e 's#$ac_boost_path_tmp/lib#$ac_boost_path_tmp/%{_lib}#' m4/boost_base.m4

%build
autoreconf -fi
%configure2_5x --disable-rpath
%make

%install
rm -rf %buildroot
%makeinstall_std

rm -f %buildroot%{_libdir}/youki/plugins/*/*.la

%{find_lang} %{name}

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/youki
%{_libexecdir}/youki-bin
%{_libexecdir}/youki-mlibman-bin
%{_libexecdir}/youki-sentinel-bin
%dir %{_libdir}/youki
%{_libdir}/youki/plugins
%{_datadir}/applications/youki.desktop
%{_datadir}/dbus-1/services/*.service
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/mpx.1.*
%{_datadir}/youki

%files -n %libname
%defattr(-, root, root)
%{_libdir}/libmpx-*.so.%{major}
%{_libdir}/libmpx-*.so.%{major}.*

%files -n %libhalcc
%defattr(-, root, root)
%{_libdir}/libhalcc-%{halcc_api}.so.%{halcc_major}
%{_libdir}/libhalcc-%{halcc_api}.so.%{halcc_major}.*

%files devel
%defattr(-, root, root)
%{_includedir}/hal++-1.0
%{_libdir}/*.so
%{_libdir}/*.la
