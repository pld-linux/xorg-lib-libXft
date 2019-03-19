Summary:	X Font Rendering library
Summary(pl.UTF-8):	Biblioteka do renderowania fontów
Name:		xorg-lib-libXft
Version:	2.3.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
# Source0-md5:	4a433c24627b4ff60a4dd403a0990796
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig-devel >= 2.5.92
BuildRequires:	freetype-devel >= 1:2.3.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.2
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	fontconfig >= 2.5.92
Requires:	freetype >= 1:2.3.0
Requires:	xorg-lib-libXrender >= 0.8.2
Obsoletes:	XFree86-xft
Obsoletes:	XFree86-xft2
Obsoletes:	Xft
Obsoletes:	libXft
Obsoletes:	xft
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

%description -l pl.UTF-8
Xft to biblioteka łącząca aplikacje X z biblioteką rasteryzacji fontów
FreeType. Do odnajdywania fontów wykorzystuje bibliotekę fontconfig,
więc Xft nie ma własnych plików konfiguracyjnych.

%package devel
Summary:	Header files for libXft library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXft
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel >= 2.5.92
Requires:	freetype-devel >= 1:2.3.0
Requires:	xorg-lib-libXrender-devel >= 0.8.2
Obsoletes:	XFree86-xft-devel
Obsoletes:	XFree86-xft2-devel
Obsoletes:	Xft-devel
Obsoletes:	libXft-devel
Obsoletes:	xft-devel

%description devel
Header files for libXft library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libXft.

%package static
Summary:	Static libXft library
Summary(pl.UTF-8):	Biblioteka statyczna libXft
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	XFree86-xft-static
Obsoletes:	Xft-static
Obsoletes:	libXft-static
Obsoletes:	xft-static

%description static
Static libXft library.

%description static -l pl.UTF-8
Biblioteka statyczna libXft.

%prep
%setup -q -n libXft-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libXft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXft.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXft.so
%{_libdir}/libXft.la
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/*.h
%{_pkgconfigdir}/xft.pc
%{_mandir}/man3/Xft.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXft.a
