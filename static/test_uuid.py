from enum import Enum


class WidthSportReview(Enum):
    required_width = [173, 220, 226, 253, 273, 299, 312, 333, 350, 360, 387, 408, 434, 505, 531, 584,
                      606, 637, 683, 700, 720]


class PresetData(Enum):
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
                   '785b0d5c-78ea-4ebc-8d58-7116a36f15e8',
                   '67463695-b649-4486-b029-934987239ece',
                   'b4de5e7a-8426-4387-ba2c-53578610fc2c',
                   '771a6cb2-4338-48b7-a21c-1c355ea70a51',
                   '2d5d852f-d9c9-48df-aa12-f6f961aeeefd',
                   '3057cb4c-87e0-4fc7-a966-3f81b5d1f613',
                   'fb5c9a8b-fe43-4e88-b5ee-5bdee095f3b3',
                   'ddc98145-e236-45cb-b8bd-0b700e8d79e2',
                   '95a5c5b7-4716-44e5-a3e0-cb73a825e873',
                   'b898ce16-2998-419c-8cae-9300567fd2cb',
                   'ad70ca7c-6ba5-40b8-8ce6-1dab390eda8e',
                   'fc83e8ee-0c62-4855-85ec-967720893816',
                   '0d6d8b42-ef8f-49c3-9115-6ab872c96028',
                   '701051e3-3cd0-4af3-88a3-e0c219bfcb79',
                   'd96089b3-3c13-4313-96c5-a63e20ad3d02',
                   '279e925c-9f2c-4294-9067-c7bc26f14c97',
                   '30541d3a-8eef-44b2-bfd9-718087c90c87',
                   'bf6d1ae7-95a5-4329-afb3-3aee5db18cb9',
                   'e49dd27f-5556-40a6-912c-0fefef6f7fd2',
                   '2e7f35b0-85d9-4a7d-a35b-4a15f9307ad4',
                   '4da982b4-af3e-4cd4-a892-5f3fdf2cb219',
                   '2a816bcd-2c8d-4f59-b148-8683e7222cf0',
                   'c452a7dd-62af-4953-9ba1-4bc5ac44bc5d',
                   '783af83e-178f-4a77-b230-8f614917c6b2',
                   '1ff28400-2f80-4b71-8bc3-98049080c5f7',
                   '251e7acf-36a0-4877-96c5-56f8176b83b7',
                   'b4611a67-2028-4abb-9e54-6dfd3d9b1b3d',
                   '373eb649-f3b4-4df8-8354-7dbe07e4eaaf',
                   'e6f88faf-981d-4319-9691-95711a570028',
                   'df238a26-b861-4fd9-8d2d-09de1fc8786a',
                   '48a38c5f-de9d-4df4-a2ad-4aa01f5f2b60',
                   '4907aa63-8a4e-4396-9985-e3e89e247e19',
                   '66db8b20-b28f-49b5-a329-0e49eec5f1cd',
                   '06577504-fd25-4110-bdb8-3352b477480b',
                   '508014cc-ee01-4bf4-8984-9776d32f56cb',
                   '7133304d-41bf-41dc-9d25-e3b4a48fc00a',
                   'a6777bf5-def6-4125-b63b-ef44ebba0e27',
                   '583679d7-f354-4fc0-99c3-59fc898ec56a',
                   '5fa82783-43af-4be7-ba32-2065bea18c02',
                   '21fa1568-6ff9-4a7b-a2ae-b39f23b5a177',
                   'd55c8c02-75c9-4e45-a81a-766808d6dc88',
                   '6e95cb33-18dd-4089-8eaa-2905eee256fb',
                   'e85e7537-8160-43c7-abc2-46057258518d',
                   '3337c100-31a6-4dd8-a84a-a9a5fff7a607',
                   '67fdaad5-ff49-4551-b920-397e9ad3dc7e',
                   '3ef95da9-5294-4f0d-9f3b-b097def3505f',
                   'bf967351-4a11-4cc7-b93f-edfccc727980',
                   'ef6cfd7a-9b12-4975-a12b-b8c88733865d',
                   '39bca739-c7d5-4c26-991b-8d6ff85aea5b']
    preset_3360 = ['333bc533-e92f-4c07-b36c-510c491f9e08',
                   '29ac7383-68f8-4ed5-a5da-88a72bb7f93c',
                   '085b68a9-5648-4d37-be18-8eea4758b57b',
                   '771a6cb2-4338-48b7-a21c-1c355ea70a51',
                   'f8dd5698-a196-4eee-bc77-a0f41b60ab66',
                   '29ea6324-75ae-4dd2-aa10-1507d706c239',
                   'f3fbea9c-a103-4b98-96ac-38c16e54eaf3',
                   '8eb61d31-992b-4b3e-b280-4d3bd80561e4',
                   '628452f6-fde9-4b83-b7ca-8a617edc80b9',
                   '1f2b5998-16c5-4e6b-a0f0-75e0c2651203',
                   '35927e3e-2261-4592-b8f1-b65a9842e18b',
                   'e6ff63f1-50e5-4827-82c9-2378db63b7d4',
                   'e04cb1e0-738d-42d7-91ad-2ecca311de75',
                   'c20b7720-6ea2-4363-bbbc-accd74c6bb12',
                   'edd4a7b8-c453-4c86-bf21-13858dd6e1b7',
                   '231f5fbc-2a93-4ad3-8053-467087039c67',
                   'd9c7c4cd-df4a-4110-91a8-52e9c446716e',
                   'ffb6872b-7783-4560-a876-06d403650c18',
                   '26578214-a4d3-45c8-80f1-a2df52d88a91',
                   '2dfc4ef1-e757-4de1-8440-da45f69eec66',
                   '45435d4a-2734-4d27-bfa4-06fb8320d632',
                   '25c68936-4691-4b9d-af1f-9f4e389e8626',
                   'b2e88363-b29e-45e8-bded-35e3ceb6c6e6']
    preset_3091 = ['4618de2f-d3a6-4d47-ba11-094a880a4ce9',
                   'bb64fd7c-0902-41a6-a203-b3023ee97a91',
                   'bf741bf1-9bfb-46de-bf0e-6106f4cfb414',
                   '6c1c0c91-165a-4cc9-823f-78c3d9c4464f',
                   '494e5373-e148-464c-9448-ec34de6b379e',
                   '088c24ec-fb15-4ff3-995d-372227ac95c1',
                   '6bdd9033-910b-4417-96ca-5f646d342620',
                   '45d9bc06-a114-4f05-a674-5f537e9e8a6b',
                   '7f422e87-41d6-43a0-8785-71baa05323e9',
                   '246f2994-a5b9-48cf-a5d6-8f8507121cb2',
                   '44d822b7-4a1f-40af-8ff7-567cc325aa5c',
                   'd5071291-6ad4-4567-ad73-a44d84b62c37',
                   'ffb5e203-7b0c-4069-b29d-38693b63334f',
                   '52942b85-dd37-4b23-b5bf-105e9c788596',
                   '22c5b6de-9f89-4179-9dba-9308bfb1a545']
    preset_3626 = ['2a800c2b-59f2-446a-af24-be58515ddf37',
                   'b5d3cd31-2757-40ca-a80d-d678b7a0ac45',
                   'cd7d1f18-f2d4-43e5-9977-a19416089169',
                   'e3743b7d-664a-46d8-978a-7f33e7df9769',
                   '1512715e-0f22-4833-9ca0-9bd6218eb1d1',
                   'ba8ed8b1-aaea-4eba-8c98-6a01fa0d9a58',
                   'e1bad081-400a-4792-9410-3d95d20b7d85',
                   'e031b32e-76eb-48b9-a697-0b0e4db94dbe',
                   'bc75ace6-65c4-449d-8b26-742f9924da14',
                   '2d7ec466-5489-49c1-9c7a-1dd2d9866be6',
                   '6c11c629-0a96-4643-95ce-7e6278543b7a',
                   'e9ed018b-ceb1-4497-9e46-83b125a500d2',
                   'c8ec8738-35a7-456a-ba34-a190eeade611',
                   '7dfe2fa4-0634-4c36-9196-a32d6b112336',
                   '2bbfe64b-d832-4e81-a72a-e05b3a2ea05d',
                   '18d22f28-8a34-4172-9047-67f3d5f6230b',
                   '929a06a6-ff35-4f7c-af77-48df0a4bbae8',
                   '94e41e3c-dddf-4865-b8e5-fb3f791653f1',
                   'd9d7b335-df20-47dc-b7fd-8fb661a586d7',
                   'e0075924-0a2d-4fec-bea4-0d6334f10243',
                   'a96c0e37-a4ac-4c30-bca0-e3c24dbc7051',
                   'b4b1473e-8f84-44cf-a522-93ed841683d6',
                   '2aeb7ee3-1e9f-47b2-803d-4b1316cd7085',
                   'a79fff85-033e-44c2-884a-ba8d5f988a17',
                   '0ec2a0db-2f0b-40ac-b935-31a5e764cd9f',
                   '667493d8-f4f9-413f-826c-6391d44f22e7',
                   '628f8720-5b96-4e39-98d7-601085745e0d',
                   '5b5e7c35-cf18-4a00-acf8-2f71adb0b866',
                   '3e1d8016-2aca-4f30-91b7-cd865e9a468c',
                   '90dd8002-02e6-4172-ad50-89f9ec5b19b2',
                   'db8437d3-b2e4-4154-8a9b-4b5d0ad4f99b',
                   '90f3172a-8c8f-47cc-90ec-8e903dcadaf0',
                   'baa0e4a9-cf99-479d-9fc7-b691ed627b1f',
                   'b775ce2a-5c68-4b37-993a-fcb82edbb989',
                   'b0d0ce95-2d04-4284-86c7-541d8e0cf7ff',
                   'b8988d01-9d58-4809-9afd-f7357b19876b',
                   'b221ecd3-27d6-4e82-b115-e4d534fdd736',
                   '969ff07f-5982-41a6-921d-59999ef68db9',
                   '3690c420-ebc9-4b70-be43-9c26e52a3be0',
                   '960facc7-b30b-4fd8-b933-07f7b1fdb2dc',
                   '82ce0fd7-1c84-4c85-8405-14af82649934',
                   '93301e0a-37d0-4868-b1f4-21bb2c953987',
                   'a555132f-16fd-4608-8427-4145953410e4',
                   '58f4f5fe-5372-4a5b-aa3b-20590c005def',
                   '50956225-18e5-4f89-8378-38332add95ed',
                   '9bd70ba5-cb8a-47c0-ade2-ee90974a9cc7',
                   'dcd9b7b5-418a-47fa-8003-d16c254db0c3']
    preset_3629 = ['5ddc6878-5233-4d14-a4f5-c9580c424502',
                   '7dab5426-a27c-43ca-8c34-b4b7d1ee641c',
                   'c557c62a-b8be-41ba-8b4c-4ce2a55ae85a',
                   'ba033a46-d032-4d2d-8289-da90d1f52363',
                   '105c63e0-6fce-4fa8-aa98-c4e87c2849a3',
                   '7a3048d9-db78-4a04-82dc-7b7f892df75e',
                   'c309da7d-0db3-45e8-9c3b-7035ad83d88f',
                   '2c561d0b-30db-4f0b-8f6a-638f8bd25677',
                   '3b4c042f-30dd-4395-9e17-85afa97a9393',
                   '02263ee9-2b00-4459-b806-922822d6b12f',
                   '22719264-37e0-4185-80f1-2f50d7711c6d',
                   '8783afd4-0ea5-4e02-b8b8-4c86e0d94ff1',
                   '87324212-64b3-40a4-b6ef-d3e552e04833',
                   '0e568c62-22bc-4458-9ac9-6d841dd41748']
    preset_3100 = ['53d5cbe4-fe48-403f-93be-9648a2b370ef']
    preset_3228 = ['f7308968-f329-4978-adce-d817e4c0bc93',
                   '1663a980-5432-4830-a38f-ebf829293ca9',
                   '5e1d11e4-128f-4a84-acc2-9917050b4f5f']


class PlaceholderPresets(Enum):
    preset_1165 = ['4028b108-2911-4660-886f-1be59093f2f3',
                   'fc46717c-dcc2-445b-af22-b1f9d4ecbec4']
    preset_1166 = ['6cd3a308-6e7f-4bb2-a7a0-d2422c4c61bd',
                   '42604215-dc83-43ce-a6bf-227087534b6b',
                   '6f96b622-01c4-4164-9e6b-d9c0b1c68f41',
                   'a74f23b9-8718-4b58-b5b3-84e56243ff52']
    preset_1167 = ['25f658c6-657a-45dc-8a5c-2ac58ede5cb0',
                   'd99d4776-c861-499d-8cf9-6980780c2fae']
    preset_3112 = ['82ed63c3-d886-4f6e-be27-20e4ff14d30d',
                   'a909449f-3899-465c-8dd3-2229a6463c5b',
                   'd512e160-ed81-4bd9-ae01-140727b362e7']
    preset_3130 = ['1070b7cb-a23d-4bd3-84d9-901e327d041b',
                   'da029398-e8d8-4f00-bbb4-c26973a3f1ba',
                   'e08b2773-5c63-467d-a8a0-9513d16d055f']
    preset_3131 = ['057a97ba-c641-40c8-9d8c-c2b10e8e14e1',
                   '0f59184b-bc6c-4491-9b80-0731c35a50bb',
                   '28cec8d2-8d6b-4e65-9350-a39fb0b0f660',
                   '468750a4-5ca7-47a6-ba37-e80e5e53e641']


class ReviewShort(Enum):
    preset_3380 = ['f9985145-c6d7-4d83-a85a-7c9cda10907f']


class TVchannels(Enum):
    tv_presets = [6401, 6405, 6416, 6425, 6429, 6440, 6451, 6455, 6466, 6475, 6484, 6491, 6525, 6534, 6541, 6552, 6559]
    tv_channel = ['3f20a7b7-62c3-4307-9b99-69cda434bad6',
                  '380ff414-7f87-4361-8124-dd0c73589693',
                  'c299b060-ca10-4c72-a099-974158ae5518',
                  '5db40733-ed15-4de8-aa55-84b3303d13d8',
                  'a1a1fa9f-8900-4166-99ef-5d2576176f65',
                  '79b91075-60b6-47f9-b830-c24cbd72538f',
                  'b221e268-f5e5-459f-9b10-81abb7b1afd1',
                  'ad0e6957-909c-4043-aed2-3f48994fac8e',
                  'e5288983-855e-44bf-a6d5-10bd903a4008',
                  'e09d2800-8636-45ad-a77d-83593504bec0']


class TitlePresets(Enum):
    presets = [1008, 1218, 1219, 1220, 1221, 1222, 1223, 1241, 1242, 1560, 1561]
    title_uuid = ['ea839f28-ed4b-424d-8df0-3baf1c62600b',
                  '9590063d-b244-4c45-9d46-a4f1fe4bbc8e',
                  'd4f35919-f519-4a64-b6f1-0bf284ce165c',
                  '6240b199-f206-49ca-8755-fa2cf98ea73a',
                  '7251dff6-4a76-4acc-be10-43a908b14ad5',
                  '23d7373d-e336-4044-a9c6-e07c9a96a06a',
                  '23d7373d-e336-4044-a9c6-e07c9a96a06a',
                  'a5cf85b2-b4a0-4b9d-b2c3-522fef227c4c',
                  'fdfdbdf4-dff3-4e1a-a41a-71643bdb9216']


class Category(Enum):
    presets = [6000, 6002, 6004, 6006, 6008, 6010]
    titles = ['R',
              'Фильмы',
              'Тестовое из пи-уай тестов',
              'Очень длинное название для категории',
              'Сериалы и прочее',
              'Попробуем через-дефис']
    category_uuid = ['b2021d79-c529-45d6-880d-94fe8cab96d4',
                     '74a0baf7-7f0c-4e2f-a284-97ef6d588d79',
                     'b90d292c-6a87-4eba-a06f-573942fc0540',
                     '2b411846-eeb9-474a-9ade-56589b888ed1',
                     '967df3a8-f39d-45b2-8d70-7c7868ba649e',
                     '946d9f49-3bef-4c93-80e7-6d6650053af7',
                     'f6ddae7d-800b-494d-962f-758a1c51b470',
                     'cab45edb-deb5-47ff-931d-1611fb8d7407',
                     'e920b424-d837-4bd9-ac4a-a4f45d996335',
                     '7313e73c-0723-4af0-868a-586939033690',  # invalid uuid
                     'dd638973-576c-4331-b926-f8b15fc63daa',
                     'c29906b1-c7ce-4800-8894-9e5f7ac8a369',
                     'abc529a6-d053-4142-8472-2343ebdad65f',
                     'b221e268-f5e5-459f-9b10-81abb7b1afd1']  # без background_portrait


class OtherPresets(Enum):
    presets = [1001, 1006, 1008, 1021, 1094, 1202, 1207, 1218, 1241, 1242, 1560, 1561, 3033, 3054, 3137, 3490, 4000]
    data_uuid = ['b08d1c98-58a4-44e6-a211-5ae7d8012b77',
                 'd943c0af-61de-469b-8517-69b78b6f0536',
                 '3341bb5e-f2b2-46db-9663-2c4e4b6f87da',
                 '436417f3-f965-4215-9ef4-3d4023461645',
                 '385c841f-9af9-45ed-ab40-e176fbd37dbf',
                 '843abd80-d588-457d-9c6c-8db49ae805bb',
                 '9be280e3-610a-4ce3-897e-43475e2fee28',
                 '4afbf03f-02c7-400c-8a61-3b62b866d52a',
                 'd30860ee-dfc2-4aa5-bc33-4cfd42f241d6',
                 '7d7d0e65-c50e-4717-89f5-d7da8f69929d',
                 'b439573b-a77a-4021-93a7-afd29f63bd43',
                 'bad50a85-d766-4169-8a27-5799d4f50259',
                 '70a3217b-573d-46f5-8064-8d721ec2b94d',
                 '23715109-a462-404a-a280-7cd564453488']


class ButtonsPresets(Enum):
    presets = [6511, 6512, 6514]
    widths = [348, 696]
    data_uuid = ['d60d4c68-b60d-412d-b6ad-393a2b3131fb',
                 '9cd7cc23-26b5-4c60-906c-4dd6ed35715a']
