#!/usr/bin/env python

import sys, os

# add libkoki/tools to path to allow inclusion of markergen
sys.path.insert(0, os.path.join(
        os.path.dirname( __file__ ), "libkoki/tools" ) )
from markergen import *

# DIMENSIONS

ARENA_WIDTH        = 250 # mm
ROBOT_WIDTH        = 100 # mm
PEDESTAL_WIDTH     = 200 # mm
TOKEN_WIDTH        = 200 # mm

ARENA_MARGIN_LEFT  = 5 # mm
ARENA_MARGIN_TOP   = 5 # mm
TOKEN_MARGIN_LEFT  = 5 # mm
TOKEN_MARGIN_TOP   = 5 # mm
PEDESTAL_MARGIN_LEFT = 5 # mm
PEDESTAL_MARGIN_TOP  = 5 # mm
ROBOT_MARGIN_LEFT  = 5 # mm
ROBOT_MARGIN_TOP   = 5 # mm

A4_WIDTH           = 210 # mm
A4_HEIGHT          = 297 # mm

A3_WIDTH           = 297 # mm
A3_HEIGHT          = 420 # mm


# FILE NAMES

SET_A_DIR          = "marker_set_a/"
SET_B_DIR          = "marker_set_b/"

ARENA_PREFIX       = "arena-"
TOKEN_PREFIX       = "token-"
PEDESTAL_PREFIX    = "pedestal-"
ROBOT_PREFIX       = "robot-"


# DESCRIPTIONS

ARENA_DESC       = "ARENA"
TOKEN_DESC       = "TOKEN"
ROBOT_DESC       = "ROBOT"
PEDESTAL_DESC       = "ROBOT"



def dir_from_code(code):

    if code >= 0 and code < 100:
        return SET_A_DIR

    elif code >= 100 and code < 200:
        return SET_B_DIR

    else:
        return None



def desc_from_code(code):

    if code >= 100:
        code -= 100

    if code <= 27:
        return ARENA_DESC

    elif code <= 31:
        return ROBOT_DESC

    elif code <= 40:
        return PEDESTAL_DESC

    elif code <= 55:
        return TOKEN_DESC

    else:
        return None


def prefix_from_code(code):

    if code >= 100:
        code -= 100

    if code <= 27:
        return ARENA_PREFIX

    elif code <= 31:
        return ROBOT_PREFIX

    elif code <= 40:
        return PEDESTAL_PREFIX

    elif code <= 55:
        return TOKEN_PREFIX

    else:
        return None



def paper_size_from_code(code):

    if code >= 100:
        code -= 100

    if code <= 27:
        return "A3"

    else:
        return "A4"



def marker_width_from_code(code):

    if code >= 100:
        code -= 100

    if code <= 27:
        return ARENA_WIDTH

    elif code <= 31:
        return ROBOT_WIDTH

    elif code <= 40:
        return PEDESTAL_WIDTH

    elif code <= 55:
        return TOKEN_WIDTH

    else:
        return None


def margins_from_code(code):

    if code >= 100:
        code -= 100

    if code <= 27:
        return (ARENA_MARGIN_LEFT, ARENA_MARGIN_TOP)

    elif code <= 31:
        return (ROBOT_MARGIN_LEFT, ROBOT_MARGIN_TOP)

    elif code <= 40:
        return (PEDESTAL_MARGIN_LEFT, PEDESTAL_MARGIN_TOP)

    elif code <= 55:
        return (TOKEN_MARGIN_LEFT, TOKEN_MARGIN_TOP)

    else:
        return None




def gen_generic(num, four_up=True):

    paper_size = paper_size_from_code(num)
    width = 0
    height = 0

    if paper_size == "A4":
        width = A4_WIDTH
        height = A4_HEIGHT

    elif paper_size == "A3":
        width = A3_WIDTH
        height = A3_HEIGHT


    s = get_pdf_surface(mm_to_pt(width),
                        mm_to_pt(height),
                        "%s%s%03d.pdf" % (dir_from_code(num), prefix_from_code(num), num))

    marker_width = marker_width_from_code(num)
    margins = margins_from_code(num)
    margin_left = margins[0]
    margin_top = margins[1]

    if four_up:

        render_marker(s, num,
                      mm_to_pt(marker_width),
                      mm_to_pt(margin_left),
                      mm_to_pt(margin_top),
                      desc_from_code(num))

        render_marker(s, num,
                      mm_to_pt(marker_width),
                      mm_to_pt(margin_left) + mm_to_pt(marker_width),
                      mm_to_pt(margin_top),
                      desc_from_code(num))

        render_marker(s, num,
                      mm_to_pt(marker_width),
                      mm_to_pt(margin_left),
                      mm_to_pt(margin_top) + mm_to_pt(marker_width),
                      desc_from_code(num))

        render_marker(s, num,
                      mm_to_pt(marker_width),
                      mm_to_pt(margin_left) + mm_to_pt(marker_width),
                      mm_to_pt(margin_top) + mm_to_pt(marker_width),
                      desc_from_code(num))

    else:

        render_marker(s, num,
                      mm_to_pt(marker_width),
                      mm_to_pt((width  - marker_width) / 2),
                      mm_to_pt((height - marker_width) / 2),
                      desc_from_code(num))


    finish_surface(s)


def gen_all():
    for i in xrange(55):
        gen_generic(i)
        gen_generic(i+100)


if __name__ == '__main__':
    gen_all()
