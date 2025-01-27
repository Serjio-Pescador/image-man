import allure
import pytest
import os, requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import time
from playwright.sync_api import Page, expect
from urllib.parse import parse_qs
# from static_data.uuid_data import football


load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

preset_3312 = ['fe8374ab-45b3-485d-aef0-3f5513c8695c',
                   'ddd33772-c71d-4160-b9ba-6b2a05f0125a',
                   '179dbec9-a225-4ffc-82f9-78006e74bd65',
                   '437de2a8-270f-419c-8365-529e774b7f09',
                   '4aeca081-e06b-482f-b875-81170387e027',
                   '03fbdbe9-41e0-41ce-9fd2-190b1335e851',
                   '21b29056-7d24-4e9e-8234-68ade2b7f173',
                   '1146bd7b-41f6-4e34-af23-2d5c79bc0c64',
                   '7d4caccd-0d1d-4372-b3b6-ad906bff2639',
                   'f1376d75-b672-43b7-8d0c-ea3d9ed15704',
                   'b5fbbd0c-3fe5-4962-bb61-3bc62bba2a92',
                   '001af628-a765-406d-be3b-4f4d67e0b825',
                   '75154114-6ad4-4f72-b979-3a22970e919c',
                   '7bdbfffd-105d-4f71-b73c-ceceee23062d',
                   'f5a9525e-98ee-4a1e-8074-2927e94ec1e9',
                   'f4441517-9d59-4b33-aeb6-2ff260bc5071',
                   '37fc53a7-43f1-406c-bcfb-520c1a794522',
                   'cb82a8da-b5fd-4c9d-b318-802278852aab',
                   'fe8374ab-45b3-485d-aef0-3f5513c8695c',
                   '785b0d5c-78ea-4ebc-8d58-7116a36f15e8',
                   '67463695-b649-4486-b029-934987239ece',
                   'b4de5e7a-8426-4387-ba2c-53578610fc2c',
                   '771a6cb2-4338-48b7-a21c-1c355ea70a51',
                   '2d5d852f-d9c9-48df-aa12-f6f961aeeefd',
                   '3057cb4c-87e0-4fc7-a966-3f81b5d1f613',
                   'fb5c9a8b-fe43-4e88-b5ee-5bdee095f3b3',
                   'ddc98145-e236-45cb-b8bd-0b700e8d79e2'
                   ]

preset_3360 = ['333bc533-e92f-4c07-b36c-510c491f9e08',
                   '29ac7383-68f8-4ed5-a5da-88a72bb7f93c',
                   '085b68a9-5648-4d37-be18-8eea4758b57b',
                   '771a6cb2-4338-48b7-a21c-1c355ea70a51'
                   ]

preset_3091 = ['4618de2f-d3a6-4d47-ba11-094a880a4ce9']

preset_3626 = ['2a800c2b-59f2-446a-af24-be58515ddf37',
                   'b5d3cd31-2757-40ca-a80d-d678b7a0ac45'
                   ]

preset_3629 = ['5ddc6878-5233-4d14-a4f5-c9580c424502',
                   '7dab5426-a27c-43ca-8c34-b4b7d1ee641c']


def make_screenshot(self, img_uuid, **kwargs):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
    self.screenshot(path=f"./screenshots/{test_name}_{img_uuid}.png", **kwargs)
    return


def compare_screenshot(self, image_snapshot, img_uuid, timeout: float = 4000, diff: float = 0.7, **kwargs):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
    screenshot = Image.open(BytesIO(self.screenshot(timeout=timeout, **kwargs)))
    image_snapshot(screenshot, f"./screenshots/{test_name}_{img_uuid}.png", diff)
    return


@allure.story('Обзоры матчей')
class TestReviews:
    @allure.title('Обзоры матчей пресет=3312')
    @pytest.mark.parametrize("review_uuid",
                             preset_3312
                             )
    def test_review_preset_3312(self, page, image_snapshot, review_uuid):

        query_tail = "presetId=3312&width=505&scale=2&quality=80&mediaType=webp"
        query_params = parse_qs(query_tail)
        width = int(query_params['width'][0])
        if width % 20 != 0:
            new_width = width + 20 - (width % 20)
        eql_query_IM = query_params.copy()
        eql_query_IM['width'] = [str(new_width)]

        query_tail_im = ("&".join(f'{k}={v[0]}' for k, v in eql_query_IM.items()))

        image_manager_url = f"{host_url}{review_uuid}?{query_tail_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        page.goto(image_manager_url)
        response = page.request.get(image_manager_url)
        # if response.status == 429:
        #     time.sleep(3)
        #     page.goto(image_manager_url)
        #     response = page.request.get(image_manager_url)
        # expect(response).to_be_ok()

        while response.status == 429:
            page.goto(image_manager_url)
            response = page.request.get(image_manager_url)
            time.sleep(3)
        expect(response).to_be_ok()
        make_screenshot(page, img_uuid=review_uuid)

        while response.status == 429:
            page.goto(stat_img_url)
            response = page.request.get(stat_img_url)
            time.sleep(3)
        expect(response).to_be_ok()
        compare_screenshot(page, image_snapshot, img_uuid=review_uuid)

    @allure.title('Обзоры матчей пресет=3360')
    @pytest.mark.parametrize("review_uuid",
                             preset_3360
                             )
    def test_review_preset_3360(self, page, image_snapshot, review_uuid):
        image_url = f"{host_url}{review_uuid}?presetId=3360&width=640&scale=2&quality=80&mediaType=webp"
        img = f"{static_url}{review_uuid}?presetId=3360&width=637&scale=2&quality=80&mediaType=webp"

        page.goto(image_url)
        make_screenshot(page, img_uuid=review_uuid)

        page.goto(img)
        compare_screenshot(page, image_snapshot, img_uuid=review_uuid)
