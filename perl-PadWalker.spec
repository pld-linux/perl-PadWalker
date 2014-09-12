#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PadWalker
Summary:	PadWalker - play with other peoples' lexical variables
Summary(pl.UTF-8):	PadWalker - igranie z cudzymi zmiennymi leksykalnymi
Name:		perl-PadWalker
Version:	1.96
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
# Source0-md5:	947686c045a636d507a7b4c4a1741dd3
URL:		http://search.cpan.org/dist/PadWalker/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/*.so
%{_mandir}/man3/*
