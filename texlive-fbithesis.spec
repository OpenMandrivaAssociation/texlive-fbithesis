%global tl_name fbithesis
%global tl_revision 21340

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2m
Release:	%{tl_revision}.1
Summary:	Computer Science thesis class for University of Dortmund
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fbithesis
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbithesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbithesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbithesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
At the department of computer science at the University of Dortmund
there are cardboard cover pages for research or internal reports like
master/phd-theses. The main function of this LaTeX2e document-class is a
replacement for the \maketitle command to typeset a title page that is
adjusted to these cover pages.

