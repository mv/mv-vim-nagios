"
" filetype: nagios
"

autocmd BufRead,BufNewFile */nagios/**/*cfg setlocal filetype=nagios
autocmd BufRead,BufNewFile */icinga/**/*cfg setlocal filetype=nagios
autocmd FileType           nagios setlocal ts=2 sts=2 sw=2 noet nosta list nowrap
autocmd FileType           nagios setlocal foldmethod=marker foldmarker={,} foldlevel=9

" vim:ft=vim:

