# TODO:
# - investigate the crashes at run
#
%define		source_name gmpc-shout
Summary:	Online stream browser plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka przeglądania strumieni internetowych dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-stream
Version:	0.15.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	http://download.sarine.nl/gmpc-0.15.5/%{source_name}-%{version}.tar.gz
# Source0-md5:	b120b136c44df877fe3de708c71e79d4
Patch0:		%{source_name}-plugins_path.patch
URL:		http://www.sarine.nl//gmpc-plugins
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.15.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Online stream browser plugin for Gnome Music Player Client.

%description -l pl.UTF-8
Wtyczka przeglądania strumieni internetowych dla odtwarzacza Gnome
Music Player Client.

%prep
%setup -qn %{source_name}-%{version}
%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/*.so
