Summary:	A software library for accesing MusicBrainz servers
Summary(pl.UTF-8):	Biblioteka umożliwiająca korzystanie z serwerów MusicBrainz
Name:		libmusicbrainz3
Version:	3.0.3
Release:	2
Epoch:		1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/libmusicbrainz-%{version}.tar.gz
# Source0-md5:	f4824d0a75bdeeef1e45cc88de7bb58a
Patch0:		%{name}-cppunit.patch
URL:		http://www.musicbrainz.org/
BuildRequires:	cmake >= 2.6
BuildRequires:	cppunit-devel
BuildRequires:	neon-devel >= 0.25
BuildRequires:	libdiscid-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%description -l pl.UTF-8
Biblioteka kliencka MusicBrainz pozwala aplikacjom na wysyłanie
zapytań do serwerów MusicBrainz, generowanie sygnatur z plików WAV
oraz tworzenie indeksów z płyt CD audio.

%package devel
Summary:	Headers for developing programs that will use libmusicbrainz
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania programów używających libmusicbrainz
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libdiscid-devel
Requires:	libstdc++-devel
Requires:	neon-devel >= 0.25

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne programistom do rozwijania aplikacji
używających biblioteki libmusicbrainz.

%prep
%setup -q -n libmusicbrainz-%{version}
%patch -P0 -p1

%build
%cmake . \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for rpm autodeps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libmusicbrainz3.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt NEWS.txt README.txt
%attr(755,root,root) %{_libdir}/libmusicbrainz3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmusicbrainz3.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmusicbrainz3.so
%{_includedir}/musicbrainz3
%{_pkgconfigdir}/libmusicbrainz3.pc
