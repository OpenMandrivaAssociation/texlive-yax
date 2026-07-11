%global tl_name yax
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	Yet Another Key System
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/yax
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yax.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yax.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
YaX is advertised as a key system, but it rather organizes attributes in
parameters, which parameters can be executed, so that YaX is halfway
between key management and macro definition (and actually hopes to
provide a user's interface). Values assigned to attributes can be
retrieved and tested in various ways, with full expandability ensured as
much as possible. Finally, YaX's syntax is a quite peculiar (as few
braces as possible), but may be customized. YaX is based on texapi and
thus requires e-TeX.

