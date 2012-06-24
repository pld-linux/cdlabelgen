%include	/usr/lib/rpm/macros.perl
Summary:	cdlabelgen - generates frontcards and traycards for CDs
Name:		cdlabelgen
Version:	1.5.0
Release:	3
License:	GPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narz�dzia/Tekst
Vendor:		B. W. Fitzpatrick <fitz@red-bean.com>
Source0:	http://www.red-bean.com/~bwf/software/cdlabelgen/%{name}-%{version}.tar.gz
URL:		http://www.red-bean.com/~bwf/software/cdlabelgen/
Requires:	perl >= 5.003
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This is BETA software! Please be gentle. cdlabelgen was designed to
simplify the process of generating labels for CD's. It originated as a
program to allow auto generation of frontcards and traycards for CD's
burned via an automated mechanism (specifically for archiving data).
Note that cdlabelgen does not actually print anything--it just spits
out postscript, which you can then do with as you please.

%description
Program ten jest w fazie beta! Prosimy o wyrozumia�o��. Cdlabelgen
napisano w celu uproszczenia procesu tworzenia etykiet na CD. Powsta�
jako projekt, kt�ry mia� pom�c w automatycznej generacji wk�adek do
pude�ek na wypalane p�yty CD (zw�aszcza przy archiwizacji danych).
Nalezy zwr�ci� uwag�, �e cdlabelgen sam w sobie nic nie drukuje,
tworzy jedynie plik postscriptowy, kt�ry mo�na samemu wydrukowa�.

%prep
%setup -q

%build
pod2man --section=1 cdlabelgen > cdlabelgen.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}}

%{__make} install BASE_DIR=$RPM_BUILD_ROOT%{_prefix}

install cdlabelgen.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf ChangeLog README $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz
%attr(755,root,root) %{_bindir}/cdlabelgen
%{_mandir}/man1/cdlabelgen.1.gz
%{_datadir}/cdlabelgen
