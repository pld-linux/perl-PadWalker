#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PadWalker
Summary:	PadWalker - play with other peoples' lexical variables
#Summary(pl):	
Name:		perl-PadWalker
Version:	0.10
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
# Source0-md5:	e6f48685932c1a1896872daf1aff9e3d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PadWalker is a module which allows you to inspect (and even change!)
lexical variables in any subroutine which called you. It will only show
those variables which are in scope at the point of the call.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

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
%{perl_vendorarch}/auto/%{pdir}/*.bs
%{_mandir}/man3/*
