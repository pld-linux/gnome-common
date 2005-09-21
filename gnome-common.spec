Summary:	Common macros useful for building GNOME packages
Summary(es):	Macros comunes útiles para construir paquetes de GNOME
Summary(pl):	Wspólne makra przydatne do budowania pakietów GNOME
Name:		gnome-common
Version:	2.12.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	817be32ab5dc7a5d56e6ec50d56100f8
Patch0:		%{name}-am-1.7.patch
Patch1:		%{name}-omf.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	autoconf >= 2.53
Requires:	automake >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l es
gnome-common provee unos macros para los módulos de GNOME.

%description -l pl
Ten pakiet dostarcza makra do budowania pakietów GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
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
