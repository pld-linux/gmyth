Summary:	Myth TV library based upon GLib/GObject paradigm
Summary(pl.UTF-8):	Biblioteka Myth TV oparta na paradygmacie GLib/GObject
Name:		gmyth
Version:	0.7.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/gmyth/%{name}-%{version}.tar.gz
# Source0-md5:	ab6b7525fd9c71cf5203f9e61abec0c3
Patch0:		%{name}-link.patch
URL:		http://gmyth.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Myth TV library based upon GLib/GObject paradigm.

%description -l pl.UTF-8
Biblioteka Myth TV oparta na paradygmacie GLib/GObject.

%package devel
Summary:	Header files for gmyth library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gmyth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	glib2-devel >= 2.0
Requires:	libxml2-devel >= 2.0

%description devel
Header files for gmyth library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gmyth.

%package static
Summary:	Static gmyth library
Summary(pl.UTF-8):	Statyczna biblioteka gmyth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmyth library.

%description static -l pl.UTF-8
Statyczna biblioteka gmyth.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/gmyth-cat
%attr(755,root,root) %{_bindir}/gmyth-ls
%attr(755,root,root) %{_libdir}/libgmyth.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmyth.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmyth.so
%{_libdir}/libgmyth.la
%{_includedir}/gmyth
%{_pkgconfigdir}/gmyth.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmyth.a
