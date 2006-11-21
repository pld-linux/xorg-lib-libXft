Summary:	X Font Rendering library
Summary(pl):	Biblioteka do renderowania fontów
Name:		xorg-lib-libXft
Version:	2.1.11
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
# Source0-md5:	a2ceaabecac47938da68e4121b0b06d5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig-devel >= 2.2
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
Xft is a font rendering library for X.

%description -l pl
Xft jest bibliotek± s³u¿±c± do renderowania fontów dla X Window.

%package devel
Summary:	Header files for libXft library
Summary(pl):	Pliki nag³ówkowe biblioteki libXft
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
Xft is a font rendering library for X.

This package contains the header files needed to develop programs that
use libXft.

%description devel -l pl
Xft jest bibliotek± s³u¿±c± do renderowania fontów dla X Window.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXft.

%package static
Summary:	Static libXft library
Summary(pl):	Biblioteka statyczna libXft
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	XFree86-xft-static
Obsoletes:	Xft-static
Obsoletes:	libXft-static
Obsoletes:	xft-static

%description static
Xft is a font rendering library for X.

This package contains the static libXft library.

%description static -l pl
Xft jest bibliotek± s³u¿±c± do renderowania fontów dla X Window.

Pakiet zawiera statyczn± bibliotekê libXft.

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
