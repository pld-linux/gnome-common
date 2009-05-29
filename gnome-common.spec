Summary:	Common macros useful for building GNOME packages
Summary(es.UTF-8):	Macros comunes útiles para construir paquetes de GNOME
Summary(pl.UTF-8):	Wspólne makra przydatne do budowania pakietów GNOME
Name:		gnome-common
Version:	2.26.0
Release:	2
License:	GPL v2
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-common/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	196daa38cb21d91da1d6ec085f1e158b
Patch0:		%{name}-omf.patch
Patch1:		%{name}-docdir.patch
Patch2:		%{name}-automake111.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
Requires:	autoconf >= 2.53
Requires:	automake >= 1:1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l es.UTF-8
gnome-common provee unos macros para los módulos de GNOME.

%description -l pl.UTF-8
Ten pakiet dostarcza makra do budowania pakietów GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--build=%{_build}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
%{_datadir}/%{name}
