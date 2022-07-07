import scrapy
import requests


class OlxScraper(scrapy.Spider):
    name = "olx-eg-scraper"

    custom_settings = {
        "LOG_FILE": "olx_eg.log",
        "ITEM_PIPELINES": {"olx_egypt.pipelines.OlxEgPipeline": 300},
    }

    listing_endpoint = "https://search.olx.com.eg/_msearch?filter_path=took%2C*.took%2C*.suggest.*.options.text%2C*.suggest.*.options._source.*%2C*.hits.total.*%2C*.hits.hits._source.*%2C*.hits.hits.highlight.*%2C*.error%2C*.aggregations.*.buckets.key%2C*.aggregations.*.buckets.doc_count%2C*.aggregations.*.buckets.complex_value.hits.hits._source%2C*.aggregations.*.filtered_agg.facet.buckets.key%2C*.aggregations.*.filtered_agg.facet.buckets.doc_count%2C*.aggregations.*.filtered_agg.facet.buckets.complex_value.hits.hits._source"

    headers = {
        "authority": "search.olx.com.eg",
        "accept": "*/*",
        "accept-language": "en,ru;q=0.9",
        "authorization": "Basic b2x4LWVnLXByb2R1Y3Rpb24tc2VhcmNoOn1nNDM2Q0R5QDJmWXs2alpHVGhGX0dEZjxJVSZKbnhL",
        "content-type": "application/x-ndjson",
        "origin": "https://www.olx.com.eg",
        "referer": "https://www.olx.com.eg/",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1879 (beta) Yowser/2.5 Safari/537.36",
    }

    cities = [
        "1-5",
        "1-68",
        "1-6",
        "1-71",
        "1-65",
        "1-57",
        "1-60",
        "1-66",
        "1-59",
        "1-70",
        "1-67",
        "1-50",
        "1-73",
        "1-69",
        "1-62",
        "1-58",
        "1-55",
        "1-61",
        "1-64",
        "1-72",
        "1-63",
        "1-77",
        "1-56",
        "1-76",
        "1-54",
        "1-74",
    ]

    city_ids = [
        "2-288",
        "2-381",
        "2-408",
        "2-332",
        "2-287",
        "2-320",
        "2-322",
        "2-263",
        "2-382",
        "2-319",
        "2-380",
        "2-269",
        "2-398",
        "2-359",
        "2-424",
        "2-385",
        "2-286",
        "2-321",
        "2-140",
        "2-295",
        "2-134",
        "2-139",
        "2-133",
        "2-131",
        "2-333",
        "2-393",
        "2-391",
        "2-132",
        "2-383",
        "2-144",
        "2-401",
        "2-289",
        "2-389",
        "2-386",
        "2-292",
        "2-136",
        "2-143",
        "2-150",
        "2-397",
        "2-142",
        "2-217",
        "2-205",
        "2-212",
        "2-213",
        "2-417",
        "2-230",
        "2-194",
        "2-210",
        "2-211",
        "2-413",
        "2-384",
        "2-222",
        "2-197",
        "2-198",
        "2-208",
        "2-195",
        "2-414",
        "2-221",
        "2-233",
        "2-207",
        "2-204",
        "2-199",
        "2-219",
        "2-201",
        "2-224",
        "2-229",
        "2-200",
        "2-202",
        "2-227",
        "2-196",
        "2-411",
        "2-206",
        "2-422",
        "2-203",
        "2-228",
        "2-317",
        "2-309",
        "2-301",
        "2-303",
        "2-113",
        "2-318",
        "2-302",
        "2-312",
        "2-119",
        "2-304",
        "2-299",
        "2-100",
        "2-390",
        "2-308",
        "2-412",
        "2-307",
        "2-109",
        "2-297",
        "2-416",
        "2-124",
        "2-106",
        "2-99",
        "2-300",
        "2-306",
        "2-305",
        "2-115",
        "2-116",
        "2-121",
        "2-311",
        "2-112",
        "2-362",
        "2-104",
        "2-125",
        "2-105",
        "2-107",
        "2-111",
        "2-96",
        "2-114",
        "2-117",
        "2-95",
        "2-387",
        "2-172",
        "2-174",
        "2-171",
        "2-173",
        "2-178",
        "2-175",
        "2-177",
        "2-79",
        "2-165",
        "2-77",
        "2-94",
        "2-166",
        "2-78",
        "2-365",
        "2-159",
        "2-377",
        "2-373",
        "2-420",
        "2-376",
        "2-370",
        "2-368",
        "2-371",
        "2-363",
        "2-372",
        "2-375",
        "2-367",
        "2-366",
        "2-369",
        "2-157",
        "2-158",
        "2-364",
        "2-374",
        "2-419",
        "2-40",
        "2-34",
        "2-35",
        "2-37",
        "2-42",
        "2-32",
        "2-27",
        "2-26",
        "2-39",
        "2-36",
        "2-38",
        "2-28",
        "2-33",
        "2-30",
        "2-41",
        "2-29",
        "2-31",
        "2-80",
        "2-87",
        "2-86",
        "2-84",
        "2-83",
        "2-82",
        "2-85",
        "2-81",
        "2-23",
        "2-19",
        "2-16",
        "2-15",
        "2-164",
        "2-415",
        "2-22",
        "2-17",
        "2-24",
        "2-25",
        "2-20",
        "2-21",
        "2-179",
        "2-409",
        "2-183",
        "2-399",
        "2-182",
        "2-180",
        "2-181",
        "2-184",
        "2-162",
        "2-89",
        "2-92",
        "2-88",
        "2-90",
        "2-91",
        "2-93",
        "2-326",
        "2-328",
        "2-327",
        "2-331",
        "2-329",
        "2-330",
        "2-325",
        "2-245",
        "2-242",
        "2-243",
        "2-247",
        "2-246",
        "2-249",
        "2-251",
        "2-250",
        "2-244",
        "2-248",
        "2-252",
        "2-396",
        "2-189",
        "2-187",
        "2-191",
        "2-193",
        "2-185",
        "2-192",
        "2-61",
        "2-57",
        "2-62",
        "2-56",
        "2-54",
        "2-55",
        "2-53",
        "2-60",
        "2-59",
        "2-58",
        "2-6",
        "2-10",
        "2-14",
        "2-127",
        "2-5",
        "2-9",
        "2-378",
        "2-11",
        "2-2",
        "2-12",
        "2-3",
        "2-1",
        "2-8",
        "2-7",
        "2-13",
        "2-4",
        "2-126",
        "2-404",
        "2-339",
        "2-341",
        "2-344",
        "2-337",
        "2-343",
        "2-342",
        "2-346",
        "2-340",
        "2-345",
        "2-338",
        "2-50",
        "2-51",
        "2-43",
        "2-49",
        "2-45",
        "2-52",
        "2-48",
        "2-47",
        "2-46",
        "2-44",
        "2-74",
        "2-76",
        "2-160",
        "2-161",
        "2-73",
        "2-75",
        "2-72",
        "2-235",
        "2-241",
        "2-234",
        "2-239",
        "2-240",
        "2-238",
        "2-236",
        "2-237",
        "2-163",
        "2-392",
        "2-63",
        "2-67",
        "2-64",
        "2-66",
        "2-69",
        "2-71",
        "2-65",
        "2-68",
        "2-70",
        "2-274",
        "2-277",
        "2-418",
        "2-316",
        "2-282",
        "2-281",
        "2-276",
        "2-283",
        "2-284",
        "2-278",
        "2-279",
        "2-280",
        "2-285",
        "2-350",
        "2-356",
        "2-347",
        "2-351",
        "2-357",
        "2-349",
        "2-353",
        "2-348",
        "2-354",
        "2-355",
        "2-265",
        "2-268",
        "2-271",
        "2-272",
        "2-270",
        "2-315",
        "2-266",
        "2-167",
        "2-334",
        "2-170",
        "2-336",
        "2-169",
        "2-335",
        "2-168",
        "2-258",
        "2-253",
        "2-254",
        "2-256",
    ]

    post_data = [
        '{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":0,"track_total_hits":false,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"category.lvl1.externalID":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.lvl0.externalID":"138"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"category.lvl1.externalID","size":20}}}}}}}}}}}},"location.lvl2":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl1.externalID":"{city}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl2.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl2"]}}}}}}}}}}}}}}}}}},"location.lvl3":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl2.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl3.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl3"]}}}}}}}}}}}}}}}}}},"product":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["product"]}}}}}}}}}}}}}}}}}},"totalProductCount":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["totalProductCount"]}}}}}}}}}}}}}}}}}}}}}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":45,"track_total_hits":200000,"query":{{"function_score":{{"random_score":{{"seed":581}},"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}}}}}},"sort":["_score"]}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":{page},"size":45,"track_total_hits":200000,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"sort":[{{"timestamp":{{"order":"desc"}}}},{{"id":{{"order":"desc"}}}}]}}\n',
        '{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":0,"track_total_hits":false,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"category.lvl1.externalID":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.lvl0.externalID":"138"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"category.lvl1.externalID","size":20}}}}}}}}}}}},"location.lvl2":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl1.externalID":"{city}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl2.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl2"]}}}}}}}}}}}}}}}}}},"location.lvl3":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl2.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl3.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl3"]}}}}}}}}}}}}}}}}}},"product":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["product"]}}}}}}}}}}}}}}}}}},"totalProductCount":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["totalProductCount"]}}}}}}}}}}}}}}}}}}}}}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":45,"track_total_hits":200000,"query":{{"function_score":{{"random_score":{{"seed":234}},"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}}}}}},"sort":["_score"]}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":{page},"size":45,"track_total_hits":200000,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"sort":[{{"_score":{{"order":"desc"}}}}]}}\n',
        '{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":0,"track_total_hits":false,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"category.lvl1.externalID":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.lvl0.externalID":"138"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"category.lvl1.externalID","size":20}}}}}}}}}}}},"location.lvl2":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl1.externalID":"{city}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl2.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl2"]}}}}}}}}}}}}}}}}}},"location.lvl3":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl2.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl3.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl3"]}}}}}}}}}}}}}}}}}},"product":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["product"]}}}}}}}}}}}}}}}}}},"totalProductCount":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["totalProductCount"]}}}}}}}}}}}}}}}}}}}}}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":45,"track_total_hits":200000,"query":{{"function_score":{{"random_score":{{"seed":936}},"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}}}}}},"sort":["_score"]}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":{page},"size":45,"track_total_hits":200000,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"sort":[{{"extraFields.price":{{"order":"asc"}}}},{{"extraFields.salary_to":{{"order":"asc"}}}},{{"id":{{"order":"desc"}}}}]}}\n',
        '{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":0,"track_total_hits":false,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"category.lvl1.externalID":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.lvl0.externalID":"138"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"category.lvl1.externalID","size":20}}}}}}}}}}}},"location.lvl2":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl1.externalID":"{city}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl2.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl2"]}}}}}}}}}}}}}}}}}},"location.lvl3":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl2.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl3.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl3"]}}}}}}}}}}}}}}}}}},"product":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["product"]}}}}}}}}}}}}}}}}}},"totalProductCount":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["totalProductCount"]}}}}}}}}}}}}}}}}}}}}}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":45,"track_total_hits":200000,"query":{{"function_score":{{"random_score":{{"seed":99}},"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}}}}}},"sort":["_score"]}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":{page},"size":45,"track_total_hits":200000,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"sort":[{{"extraFields.price":{{"order":"desc"}}}},{{"extraFields.salary_to":{{"order":"desc"}}}},{{"id":{{"order":"desc"}}}}]}}\n',
    ]

    def start_requests(self):
        for data in self.post_data:
            for city in self.cities:
                for _id in self.city_ids:
                    for i in range(0, 9911):
                        page = i + 45
                        yield scrapy.Request(
                            url=self.listing_endpoint,
                            method="POST",
                            headers=self.headers,
                            body=data.format(city=city, _id=_id, page=page),
                            callback=self.parse_links,
                        )

    def parse_links(self, response):
        if "hits" in response.json()["responses"][1]["hits"]:
            try:
                listing_data = response.json()["responses"][2]["hits"]["hits"]
            except:
                listing_data = response.json()["responses"][1]["hits"]["hits"]

            for listing in listing_data:
                listing_id = listing["_source"]["externalID"]
                listing_url = "https://www.olx.com.eg/en/ad/" + listing_id

                yield scrapy.Request(
                    url=listing_url,
                    headers=self.headers,
                    callback=self.parse_details,
                    meta={"listing_url": listing_url},
                )

    def parse_details(self, response):
        item = {}
        reference_id = response.css("div._171225da::text").get().replace("Ad id ", "")
        sub_detail_list = response.css("div._676a547f ::text").extract()

        item["URL"] = response.meta.get("listing_url")
        try:
            item["Breadcrumb"] = (
                response.css("li._8c543153 ::text")[4].get()
                + "/"
                + response.css("li._8c543153 ::text")[3].get()
                + "/"
                + response.css("li._8c543153 ::text")[2].get()
                + "/"
                + response.css("li._8c543153 ::text")[1].get()
                + "/"
                + response.css("li._8c543153 ::text").get()
            )
        except:
            item["Breadcrumb"] = (
                +response.css("li._8c543153 ::text")[3].get()
                + "/"
                + response.css("li._8c543153 ::text")[2].get()
                + "/"
                + response.css("li._8c543153 ::text")[1].get()
                + "/"
                + response.css("li._8c543153 ::text").get()
            )

        item["Price"] = response.css("span._56dab877 ::text").get()
        item["Title"] = response.css("h1.a38b8112::text").get()
        item["Type"] = response.css("div.b44ca0b3 ::text")[1].get()
        item["Bedrooms"] = response.css("span.c47715cd::text").get()
        try:
            item["Bathrooms"] = response.css("span.c47715cd::text")[1].get()
        except:
            item["Bathrooms"] = ""
        try:
            item["Area"] = response.css("span.c47715cd::text")[2].get()
        except:
            for sub in sub_detail_list:
                if "Area (m²)" in sub_detail_list:
                    item["Area"] = sub_detail_list[
                        sub_detail_list.index("Area (m²)") + 1
                    ]
                else:
                    item["Area"] = ""
        item["Location"] = response.css("span._8918c0a8::text").get()
        try:
            if response.css("div.b44ca0b3 ::text")[18].get() == "Compound":
                item["Compound"] = response.css("div.b44ca0b3 ::text")[19].get()
            elif response.css("div.b44ca0b3 ::text")[16].get() == "Compound":
                item["Compound"] = response.css("div.b44ca0b3 ::text")[17].get()
        except:
            item["Compound"] = ""
        item["seller"] = response.css("span._261203a9._2e82a662::text").getall()[1]
        member_since = response.css("span._34a7409b ::text")[1].get()
        if member_since == "Cars for Sale":
            item["Seller_member_since"] = response.css("span._34a7409b ::text").get()
        if "Commercial ID: " in member_since:
            item["Seller_member_since"] = response.css("span._34a7409b ::text")[2].get()
        else:
            item["Seller_member_since"] = member_since
        res = requests.get(
            f"https://www.olx.com.eg/api/listing/{reference_id}/contactInfo/"
        )
        item["Seller_phone_number"] = res.json()["mobile"]
        item["Description"] = (
            response.css("div._0f86855a ::text").get().replace("\n", "")
        )
        item["Amenities"] = ",".join(response.css("div._27f9c8ac ::text").extract())
        item["Reference"] = reference_id
        item["Listed_date"] = response.css("span._8918c0a8 ::text")[1].get()
        item["Level"] = ""
        item["Payment_option"] = ""
        item["Delivery_term"] = ""
        item["Furnished"] = ""
        item["Delivery_date"] = ""
        item["Down_payment"] = ""

        for sub_detail in sub_detail_list:
            if "Level" in sub_detail_list:
                item["Level"] = sub_detail_list[sub_detail_list.index("Level") + 1]
            if "Payment Option" in sub_detail_list:
                item["Payment_option"] = sub_detail_list[
                    sub_detail_list.index("Payment Option") + 1
                ]
            if "Delivery Term" in sub_detail_list:
                item["Delivery_term"] = sub_detail_list[
                    sub_detail_list.index("Delivery Term") + 1
                ]
            if "Furnished" in sub_detail_list:
                item["Furnished"] = sub_detail_list[
                    sub_detail_list.index("Furnished") + 1
                ]
            if "Delivery Date" in sub_detail_list:
                item["Delivery_date"] = sub_detail_list[
                    sub_detail_list.index("Delivery Date") + 1
                ]
            if "Down Payment" in sub_detail_list:
                item["Down_payment"] = sub_detail_list[
                    sub_detail_list.index("Down Payment") + 1
                ]

        item["Image_url"] = response.css("picture._219b7e0a ::attr(srcset)")[1].get()

        yield item
