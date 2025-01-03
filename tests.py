from datetime import datetime, timezone

from source import get_stack_for_frame


def test_get_stack_for_frame_asc():
    stack = get_stack_for_frame(23474)
    assert stack[-2:] == [
        {
            'date': datetime(2024, 12, 22, 1, 0, 48, 540753, tzinfo=timezone.utc),
            'granules': [
                'S1A_IW_SLC__1SDV_20241222T010139_20241222T010206_057098_0704D4_BDC8',
                'S1A_IW_SLC__1SDV_20241222T010114_20241222T010141_057098_0704D4_184B',
                'S1A_IW_SLC__1SDV_20241222T010048_20241222T010116_057098_0704D4_A865',
            ]
        },
        {
            'date': datetime(2025, 1, 3, 1, 0, 47, 359677, tzinfo=timezone.utc),
            'granules': [
                'S1A_IW_SLC__1SDV_20250103T010137_20250103T010204_057273_070BB6_CD45',
                'S1A_IW_SLC__1SDV_20250103T010113_20250103T010140_057273_070BB6_1133',
                'S1A_IW_SLC__1SDV_20250103T010047_20250103T010115_057273_070BB6_99C5',
            ],
        }
    ]


def test_get_stack_for_frame_desc():
    stack = get_stack_for_frame(24640)
    assert stack[-3:] == [
        {
            'date': datetime(2024, 12, 10, 13, 3, 13, 352107, tzinfo=timezone.utc),
            'granules': [
                'S1A_IW_SLC__1SDV_20241210T130339_20241210T130406_056930_06FE1E_0B9C',
                'S1A_IW_SLC__1SDV_20241210T130313_20241210T130341_056930_06FE1E_4D8D',
            ],
        },
        {
            'date': datetime(2024, 12, 22, 13, 3, 12, 122492, tzinfo=timezone.utc),
            'granules': [
                'S1A_IW_SLC__1SDV_20241222T130337_20241222T130404_057105_070529_DC29',
                'S1A_IW_SLC__1SDV_20241222T130312_20241222T130340_057105_070529_0B54',
            ],
        },
        {
            'date': datetime(2025, 1, 3, 13, 3, 10, 820811, tzinfo=timezone.utc),
            'granules': [
                'S1A_IW_SLC__1SDV_20250103T130336_20250103T130403_057280_070C0A_22A9',
                'S1A_IW_SLC__1SDV_20250103T130310_20250103T130338_057280_070C0A_89D9',
            ],
        }
    ]
