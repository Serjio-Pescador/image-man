from enum import Enum


class LinkData(Enum):
    tusd_valid = ['tusd:5c1df49d969cf7ec6f823d702dad0213',
                  'tusd:04fa5fb2dc82fc069848bc7d9e1e273b?presetid=001',
                  'tusd:04fa5fb2dc82fc069848bc7d9e1e273b?size=810x540',
                  'vp-tusd-prod:fbdc25f798d58c180c84ef8002cb37c9',
                  'vp-tusd-prod:fbdc25f798d58c180c84ef8002cb37c9?presetid=001',
                  'vp-tusd-prod:fbdc25f798d58c180c84ef8002cb37c9?size=810x540']
    base64_tusd = ['[dHVzZDo1YzFkZjQ5ZDk2OWNmN2VjNmY4MjNkNzAyZGFkMDIxMw]',
                   '[dHVzZDowNGZhNWZiMmRjODJmYzA2OTg0OGJjN2Q5ZTFlMjczYg]?presetid=001',
                   '[dHVzZDowNGZhNWZiMmRjODJmYzA2OTg0OGJjN2Q5ZTFlMjczYg]?size=810x540',
                   '[dnAtdHVzZC1wcm9kOmZiZGMyNWY3OThkNThjMTgwYzg0ZWY4MDAyY2IzN2M5]',
                   '[dnAtdHVzZC1wcm9kOmZiZGMyNWY3OThkNThjMTgwYzg0ZWY4MDAyY2IzN2M5]?presetid=001',
                   '[dnAtdHVzZC1wcm9kOmZiZGMyNWY3OThkNThjMTgwYzg0ZWY4MDAyY2IzN2M5]?size=810x540']
    base64_external = ['[b2JzOi8vdnAtdHVzZC1wcm9kL2tsaXB5LzIwMjMtMTItMDgvREVCUlklMjAtJTIwJUQwJTk0JUQwJTlFJUQwJUEwJUQwJTlFJUQwJTkzJUQwJTk4JUQwJTk1JTIwJUQwJTlBJUQwJTkwJUQwJTlDJUQwJTlEJUQwJTk4L2NvdmVyLmpwZw]?size=1920x1080',
                  '[b2JzOi8vdnAtdHVzZC1wcm9kL2tsaXB5LzIwMjMtMTItMDgvREVCUlkgLSDQlNCe0KDQntCT0JjQlSDQmtCQ0JzQndCYL2NvdmVyLmpwZw]?size=1920x1080',
                  '[b2JzOi8vdnAtdHVzZC1wcm9kL2tsaXB5LzIwMjQtMDMtMjYv0L_QvtC70Y8g0LTRg9C00LrQsCAtINGB0LrRg9GH0LDRjiAo0L_RgNC-INGB0LzQtdGA0YLRjCkvY292ZXIuanBn]?width=1920',
                       '%5BaHR0cHM6Ly9jZG40Mi56dnVrLmNvbS9waWM_dHlwZT1hcnRpc3QmaWQ9Mjk0MTc2%5D',
                       '[aHR0cHM6Ly9jZG40Mi56dnVrLmNvbS9waWM_dHlwZT1hcnRpc3QmaWQ9Mjk0MTc2]',
                       '[aHR0cHM6Ly9jZG40Mi56dnVrLmNvbS9waWM_dHlwZT1hcnRpc3QmaWQ9Mjk0MTc2]?presetid=001',
                       '[aHR0cHM6Ly9jZG41Mi56dnVrLmNvbS9waWM_dHlwZT1yZWxlYXNlJmlkPTE0NjQwNjMy]?size=300x300',
                       '[aHR0cHM6Ly9jZG41MS56dnVrLmNvbS9waWM_dHlwZT1yZWxlYXNlJmlkPTMwOTYxMjI0]',
                       '[aHR0cHM6Ly9jZG42Ni56dnVrLmNvbS9waWM_dHlwZT1yZWxlYXNlJmlkPTMzMjI3NDQ]',
                       '[aHR0cHM6Ly9ibG9nLm9ra28udHYvdGh1bWIvc21hcnQvaW1ncy8yMDI0LzA4LzA3LzE3LzY1NTU4NDMvYWQxOGYxZmNiYTk3ZWNiYzFlZjUxNGZiMDYxN2E3MDZiY2FhMTNjNi5qcGVn]',
                       '[aHR0cHM6Ly9jZG42Mi56dnVrLmNvbS9waWM_dHlwZT1yZWxlYXNlJmlkPTMzMjI3NDY]?presetid=002',
                       '[aHR0cHM6Ly9zdGF0aWMub2trby50di9pbWFnZXMvdjQvMTE1YmYwOGUtOWIwNS00ZDlkLTkwMjQtOTQ1Yjk5YzE3NmIw]',
                       '[aHR0cHM6Ly9wcmUtc3RhdGljLm9ra28udHYvaW1hZ2VzL3Y0L2FjZDNiNDUxLTJkN2UtNDVhYi1hODY3LWFhZGY5ZWYyYmYwNw]',
                       '[aHR0cHM6Ly9jbGllbnRzLXN0YXRpYy5va2tvLnR2L2dyYXBoaWNzL21lbnUvZXVyby9tZW51X3Nwb3J0X2V1cm8ucG5n]',
                       '[aHR0cHM6Ly9wcmUtc3RhdGljLm9ra28udHYvaW1hZ2VzL3YyL2dldFdhdGVybWFyaz9kYXRhPWh0dHBzOi8vd3d3LmZvbi5iZXQ_dXRtX3NvdXJjZT1va2tv]',
                       "[aHR0cHM6Ly9wcmUtc3RhdGljLm9ra28udHYvaW1hZ2VzL3YyL2dldFdhdGVybWFyaz9kYXRhPWh0dHBzOi8vd3d3LmZvbi5iZXQ_dXRtX3NvdXJjZT1va2tv]?presetId=7001",
                       '[aHR0cHM6Ly94bWwtZXBnc2VydmljZS5jZG52aWRlby5ydS9FUEdTZXJ2aWNlL2hzL3htbGRhdGEvZmZkYTFkNDItZTI4Zi00ZWFjLWFmMWQtMDU5NWQ5OTAyZGMvcGljLzU1MzUzMzg]',
                       ]

class LinkNotValid(Enum):
    tusd_invalid = ['test:04fa5fb2dc82fc069848bc7d9e1e273b',
                    'tusd:04fa5fb2dc82fc069848bc7d9e1e273z',
                    'tusd:48b538cccb3a2a94b849b719347093df']

    link_invalid = ['[dGVzdDowNGZhNWZiMmRjODJmYzA2OTg0OGJjN2Q5ZTFlMjczYg]',
                    '[dHVzZDowNGZhNWZiMmRjODJmYzA2OTg0OGJjN2Q5ZTFlMjczeg]',
                    '[dHVzZDo0OGI1MzhjY2NiM2EyYTk0Yjg0OWI3MTkzNDcwOTNkZg]',
                    '[aHR0cHM6Ly9jZG42Mi56dnVrLmNvbS9waWM/dHlwZT1yZWxlYXNlJmlkPTE]',
                    '[aHR0cHM6Ly9jZG42Mi56dnVrLmNvbS9waWM/dHlwZT1yZWxlYXNlJmlkPTMzMjI3NDY=]',
                    '[test_link]']
    not_white_list = ['[aHR0cHM6Ly92ay5jb20v]',
                      '[https://clients-static.okko.tv/graphics/logo/okko/okko-8march-full.png]']