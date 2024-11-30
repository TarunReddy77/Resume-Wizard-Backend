from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Constants
INCH_TO_EMU = 914440
INCH_TO_TWIPS = 2000

MARGIN = 0.3

FONT_SETTINGS = {
    'font': 'Calibri',
    'size': {
        'name': Pt(15),
        'contact_info': Pt(11),
        'section_heading': Pt(11),
        'infocard_heading': Pt(11),
        'infocard_subheading': Pt(11),
        'bullet_points': Pt(10),
        'skills': Pt(10)
    },
    'style': {
        'name': {
            'bold': True,
            'italic': False
        },
        'contact_info': {
            'bold': False,
            'italic': False,
            'delimiter': ' | '
        },
        'section_heading': {
            'bold': True,
            'italic': False
        },
        'infocard_heading_title': {
            'bold': True,
            'italic': False
        },
        'infocard_heading_timeline': {
            'bold': False,
            'italic': False
        },
        'infocard_subheading': {
            'bold': False,
            'italic': False
        },
        'bullet_points': {
            'bold': False,
            'italic': False
        },
        'skills_category': {
            'bold': True,
            'italic': False
        },
        'skills_tools': {
            'bold': False,
            'italic': True
        }
    },
    'color': {
        'name': RGBColor(0, 0, 0),
        'contact_info': RGBColor(0, 0, 0),
        'section_heading': RGBColor(0, 0, 0),
        'infocard_heading': RGBColor(0, 0, 0),
        'infocard_subheading': RGBColor(0, 0, 0),
        'bullet_points': RGBColor(0, 0, 0),
        'skills': RGBColor(0, 0, 0)
    }
}

MARGIN_SETTINGS = {
    'top': int(MARGIN * INCH_TO_EMU),
    'bottom': int(MARGIN * INCH_TO_EMU),
    'left': int(MARGIN * INCH_TO_EMU),
    'right': int(MARGIN * INCH_TO_EMU)
}

PAGE_SETTINGS = {
    'width': int(8.5 * INCH_TO_EMU),
    'height': int(11 * INCH_TO_EMU)
}

SPACING_SETTINGS = {
    'name': {
        'before': Pt(0),
        'after': Pt(1),
        'line_spacing': 1
    },
    'contact_info': {
        'before': Pt(0),
        'after': Pt(1),
        'line_spacing': 1
    },
    'section_heading': {
        'before': Pt(8),
        'after': Pt(4),
        'line_spacing': 1
    },
    'infocard_heading_title': {
        'before': Pt(1),
        'after': Pt(0),
        'line_spacing': 1
    },
    'infocard_heading_timeline': {
        'before': Pt(1),
        'after': Pt(0),
        'line_spacing': 1
    },
    'infocard_subheading': {
        'before': Pt(0),
        'after': Pt(0),
        'line_spacing': 1
    },
    'bullet_points': {
        'before': Pt(0),
        'after': Pt(0),
        'line_spacing': 1
    },
    'skills': {
        'before': Pt(0),
        'after': Pt(0),
        'line_spacing': 1
    },
    'skills_category': {
        'before': Pt(0),
        'after': Pt(0),
        'line_spacing': 1
    },
    'skills_tools': {
        'before': Pt(0),
        'after': Pt(0),
        'line_spacing': 1
    }
}

ALIGNMENT_SETTINGS = {
    'name': WD_PARAGRAPH_ALIGNMENT.CENTER,
    'contact_info': WD_PARAGRAPH_ALIGNMENT.CENTER,
    'section_heading': WD_PARAGRAPH_ALIGNMENT.LEFT,
    'infocard_heading_title': WD_PARAGRAPH_ALIGNMENT.LEFT,
    'infocard_heading_timeline': WD_PARAGRAPH_ALIGNMENT.RIGHT,
    'infocard_subheading': WD_PARAGRAPH_ALIGNMENT.LEFT,
    'skills_table': WD_PARAGRAPH_ALIGNMENT.CENTER,
    'skills': WD_PARAGRAPH_ALIGNMENT.LEFT,
    'skills_category': WD_PARAGRAPH_ALIGNMENT.LEFT,
    'skills_tools': WD_PARAGRAPH_ALIGNMENT.LEFT,
    'bullet_points': WD_PARAGRAPH_ALIGNMENT.LEFT,
}

INDENTATION_SETTINGS = {
    'bullet_points': {
        'left': int(0.25 * INCH_TO_EMU),
        'right': 0,
        'first_line': int(-0.15 * INCH_TO_EMU)
    }
}

TABLE_SETTINGS = {
    'event_table': {
        'first_col_width': int(6.5 * INCH_TO_EMU),
        'second_col_extra_width': int(0.16 * INCH_TO_EMU)
    },
    'skills_table': {
        'first_col_width': int(2.5 * INCH_TO_EMU),
        'row_height': int(0.15)
    }
}

HYPERLINKS = ['linkedin', 'github']
