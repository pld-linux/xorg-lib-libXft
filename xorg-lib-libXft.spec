#
# Conditional build:
%bcond_without	lcd             # use own LCD filtering instead of freetype's
#
Summary:	X Font Rendering library
Summary(pl.UTF-8):	Biblioteka do renderowania fontów
Name:		xorg-lib-libXft
Version:	2.1.12
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/libXft-%{version}.tar.bz2
# Source0-md5:	1309301e2d979bd475dc58325cb8c056
Patch0:		%{name}-lcd-filter.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig-devel >= 2.2
%{?with_lcd:BuildRequires:	freetype-devel >= 1:2.3.0}
%{!?with_lcd:BuildRequires:	freetype-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.2
BuildRequires:	xorg-util-util-macros
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
Requires:	fontconfig-devel >= 2.2
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
%{?with_lcd:%patch0 -p1}

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXft.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xft-config
%attr(755,root,root) %{_libdir}/libXft.so
%{_libdir}/libXft.la
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/*.h
%{_pkgconfigdir}/xft.pc
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXft.a
