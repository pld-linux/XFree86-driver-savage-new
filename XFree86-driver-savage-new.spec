Summary:	New version of S3 Savage driver for XFree86
Summary(pl):	Nowa wersja sterownika S3 Savage dla XFree86
Name:		XFree86-driver-savage-new
Version:	1.1.18bld2
Release:	1
License:	MIT
Group:		X11/XFree86
Source0:	http://www.linux.org.uk/~alan/S3.zip
# Source0-md5:	8b754fc6bbded60b683563b945e384b0
Patch0:		XFree86-new-s3-nodebug.patch
Patch1:		XFree86-new-s3-pScreen.patch
Patch2:		XFree86-new-s3-headers.patch
BuildRequires:	XFree86-Xserver-devel > 1:4.3.99.902-0.1
BuildRequires:	ed
Obsoletes:	XFree86-driver-savage
%{requires_eq_to XFree86-Xserver XFree86-Xserver-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
New version of S3 Savage driver for XFree86.

%description -l pl
Nowa wersja sterownika S3 Savage dla XFree86.

%prep
%setup -q -c
tar xzf %{version}.tar.gz
%patch0 -p0
%patch1 -p1
%patch2 -p1

chmod u+w LinuxDriver/2D/Imakefile
echo -e ',s#$(XF86OSSRC)/vbe#$(XF86SRC)/vbe#g\n,w' | ed LinuxDriver/2D/Imakefile

%build
cd LinuxDriver/2D
xmkmf
%{__make} \
	TOP=/usr/X11R6/include/X11/Xserver \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags} -I/usr/X11R6/include/X11 -I/usr/X11R6/include/X11/extensions -I/usr/X11R6/include/X11/fonts"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/modules/drivers

install LinuxDriver/2D/savage_drv.o $RPM_BUILD_ROOT%{_libdir}/modules/drivers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/savage_drv.o
