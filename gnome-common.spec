Summary:	Common macros useful for building gnome packages
Summary(pl):	Wspólne makra przydatne do budowania pakietów GNOME
Name:		gnome-common
Version:	1.2.4
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/1.2/%{name}-%{version}.tar.bz2
# Source0-md5: 4b430c6443860e01e4bd89cadf82649b
URL:		http://www.gnome.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l pl
Ten pakiet dostarcza makra do budowania pakietów GNOME.

%prep
%setup -q

%build
%configure --build=%{_build}

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
%{_aclocaldir}/gnome-macros
%{_aclocaldir}/gnome2-macros
