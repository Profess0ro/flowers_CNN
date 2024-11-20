from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_dataset_distribution import page_dataset_body
from app_pages.page_flower_classifier import page_classifier_body
from app_pages.page_hypotheses import page_hypotheses_body
from app_pages.page_performance_metrics import page_performance_body


app = MultiPage(app_name='Flower-bingo', default_page={'title': 'Project Summary', 'function': page_summary_body})

app.add_page('Project Summary', page_summary_body)
app.add_page('Dataset distribution', page_dataset_body)
app.add_page('Flower classifier', page_classifier_body)
app.add_page('Project hypotheses', page_hypotheses_body)
app.add_page('ML Performance metrics', page_performance_body)

app.run()