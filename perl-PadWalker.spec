#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%define		pdir	PadWalker
Summary:	PadWalker - play with other peoples' lexical variables
Summary(pl.UTF-8):	PadWalker - igranie z cudzymi zmiennymi leksykalnymi
Name:		perl-PadWalker
Version:	2.5
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
# Source0-md5:	f3f1e06c0385aab80353176a414f02b2
URL:		https://metacpan.org/release/PadWalker
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PadWalker is a Perl module which allows you to inspect (and even
change!) lexical variables in any subroutine which called you. It will
only show those variables which are in scope at the point of the call.

%description -l pl.UTF-8
PadWalker jest modułem Perla umożliwiającym przeglądanie (a nawet
modyfikacje!) zmiennych leksykalnych w dowolnej wywołanej funkcji.
Pokazuje on tylko te zmienne, których zasięg obejmuje miejsce
wywołania.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/PadWalker.pm
%dir %{perl_vendorarch}/auto/PadWalker
%attr(755,root,root) %{perl_vendorarch}/auto/PadWalker/PadWalker.so
%{_mandir}/man3/PadWalker.3pm*
