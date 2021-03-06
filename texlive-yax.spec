# revision 21183
# category Package
# catalog-ctan /macros/generic/yax
# catalog-date 2011-01-23 17:05:29 +0100
# catalog-license lppl
# catalog-version 1.03
Name:		texlive-yax
Version:	1.03
Release:	11
Summary:	Yet Another Key System
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/yax
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yax.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yax.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
YaX is advertised as a key system, but it rather organizes
attributes in parameters, which parameters can be executed, so
that YaX is halfway between key management and macro definition
(and actually hopes to provide a user's interface). Values
assigned to attributes can be retrieved and tested in various
ways, with full expandability ensured as much as possible.
Finally, YaX's syntax is a quite peculiar (as few braces as
possible), but may be customized. YaX is based on texapi and
thus requires e-TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/yax/t-yax.tex
%{_texmfdistdir}/tex/generic/yax/yax.sty
%{_texmfdistdir}/tex/generic/yax/yax.tex
%doc %{_texmfdistdir}/doc/generic/yax/README
%doc %{_texmfdistdir}/doc/generic/yax/yax-doc.pdf
%doc %{_texmfdistdir}/doc/generic/yax/yax-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.03-2
+ Revision: 757741
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.03-1
+ Revision: 719962
- texlive-yax
- texlive-yax
- texlive-yax

