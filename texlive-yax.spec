Name:		texlive-yax
Version:	54080
Release:	2
Summary:	Yet Another Key System
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/yax
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yax.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yax.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
