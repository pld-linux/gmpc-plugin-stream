# TODO:
# - investigate the crashes at run
#
%define		source_name gmpcstream
Summary:	Online stream browser plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka przeglądania strumieni internetowych dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-stream
Version:	0.1.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	%{source_name}-%{version}.tar.gz
# Source0-md5:	da8341cf96d9e3885bd78a56ef13cd03
Patch0:		%{name}-plugins_path.patch
URL:		http://sarine.nl/gmpc-plugins-autoplaylist
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.14.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libtool
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
%{_datadir}/gmpc/osb.glade
