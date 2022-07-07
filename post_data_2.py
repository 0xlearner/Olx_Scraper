city = "1-5"
_id = "2-288"
page = 55

newly_listed_post_data = '{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":0,"track_total_hits":false,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"category.lvl1.externalID":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.lvl0.externalID":"138"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"category.lvl1.externalID","size":20}}}}}}}}}}}},"location.lvl2":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl1.externalID":"{city}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl2.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl2"]}}}}}}}}}}}}}}}}}},"location.lvl3":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.lvl2.externalID":"{_id}"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"location.lvl3.externalID","size":40}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["location.lvl3"]}}}}}}}}}}}}}}}}}},"product":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["product"]}}}}}}}}}}}}}}}}}},"totalProductCount":{{"global":{{}},"aggs":{{"filtered_agg":{{"filter":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}}]}}}},"aggs":{{"facet":{{"terms":{{"field":"product","size":20}},"aggs":{{"complex_value":{{"top_hits":{{"size":1,"_source":{{"include":["totalProductCount"]}}}}}}}}}}}}}}}}}}}}}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":45,"track_total_hits":200000,"query":{{"function_score":{{"random_score":{{"seed":99}},"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"product":"featured"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}}}}}},"sort":["_score"]}}\n{{"index":"olx-eg-production-ads-ar"}}\n{{"from":0,"size":0,"track_total_hits":200000,"query":{{"bool":{{"must":[{{"term":{{"category.slug":"properties"}}}},{{"term":{{"location.externalID":"{_id}"}}}}]}}}},"sort":[{{"extraFields.price":{{"order":"desc"}}}},{{"extraFields.salary_to":{{"order":"desc"}}}},{{"id":{{"order":"desc"}}}}]}}\n'
print(newly_listed_post_data.format(city=city, _id=_id, page=page))


# print(
#     newly_listed_post_data.format(
#         str(_id),
#         str(_id),
#         str(city),
#         str(_id),
#         str(_id),
#         str(_id),
#         page,
#         str(_id),
#     )
# )
