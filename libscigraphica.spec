%define	name	libscigraphica
%define	version	2.1.1
%define	release	%mkrel 11

%define realname scigraphica

%define major 2.1
%define libname %mklibname %{realname} %major
%define libnamedev %mklibname %{realname} -d


Summary: Data analysis and technical graphics library
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Libraries
URL: https://scigraphica.sourceforge.net/
Source: http://prdownloads.sourceforge.net/scigraphica/%{name}-%{version}.tar.bz2
Patch0: libscigraphica-2.1.1-fix-linkage.patch
Patch1: libscigraphica-2.1.1-fix-str-fmt.patch
Patch2: libscigraphica-2.1.1-fix-build.patch
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: perl-XML-Parser
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: gtk+extra-2-devel
BuildRequires: python-numpy-devel
BuildRequires: python-devel

%description
SciGraphica is a scientific application for data analysis and technical
graphics. It pretends to be a clone of the popular commercial (and expensive)
application "Microcal Origin". It fully supplies plotting features for 2D, 3D
and polar charts. The aim is to obtain a fully-featured, cross-platform,
user-friendly, self-growing scientific application. It is free and
open-source, released under the GPL license.


%package -n %{libname}
Summary: Library for scigraphica 
Group: Development/Other

%description -n %{libname}
SciGraphica is a scientific application for data analysis and technical
graphics. It pretends to be a clone of the popular commercial (and expensive)
application "Microcal Origin". It fully supplies plotting features for 2D, 3D
and polar charts. The aim is to obtain a fully-featured, cross-platform,
user-friendly, self-growing scientific application. It is free and
open-source, released under the GPL license.

%package -n %{libnamedev}
Summary: Libscigraphica library headers and development libraries
Group: Development/Other
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}
Provides: libscigraphica-devel
Provides: libscigraphica2-devel
Obsoletes: %{_lib}scigraphica2.1-devel

%description -n %{libnamedev}
Libscigraphica devel files


%prep
%setup -q
%patch0 -p0
%patch1 -p0 
%patch2 -p0

%build
%configure2_5x --with-python-numeric-path=%{py_platsitedir}/numpy
%make

%install
rm -fr %buildroot
%makeinstall_std

%find_lang %name

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname} -f %name.lang
%defattr(-,root,root)
%{_libdir}/*.so.*
%dir %_datadir/pixmaps/%name
%_datadir/pixmaps/%name/*.xpm
%_datadir/pixmaps/*.xpm
%dir %{_libdir}/%{realname}
%{_libdir}/%{realname}/2.1.0/plugins/*/*.so
%{_libdir}/%{realname}/2.1.0/plugins/*/*.xml

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/aclocal/*
%_datadir/pixmaps/%name/*.h
%{_libdir}/%{realname}/2.1.0/plugins/*/*.*a


