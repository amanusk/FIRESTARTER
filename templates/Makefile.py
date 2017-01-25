###############################################################################
# FIRESTARTER - A Processor Stress Test Utility
# Copyright (C) 2017 TU Dresden, Center for Information Services and High
# Performance Computing
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact: daniel.hackenberg@tu-dresden.de
###############################################################################

def target_all(file,targets):
    file.write("all: {}\n".format(targets))

def src_obj_files(file,templates,version):
    obj_files = ''
    src_files = ''
    for each in templates:
        src_files = each.file+'.c '+src_files
        obj_files = each.file+'.o '+obj_files
    file.write("ASM_FUNCTION_SRC_FILES="+src_files+"\n")
    if version.enable_win64 == 1:
        file.write("ASM_FUNCTION_SRC_FILES_WIN=sse2_functions.c avx_functions.c fma_functions.c\n")
    file.write("ASM_FUNCTION_OBJ_FILES="+obj_files+"\n")

def template_rules(file,templates):
    for each in templates:
        flags = ''
        for flag in each.flags:
            flags = flag+' '+flags
        file.write(each.file+".o: "+each.file+".c\n")
        file.write("\t${LINUX_CC} ${OPT_ASM} ${LINUX_C_FLAGS} "+flags+" -c "+each.file+".c\n\n")

