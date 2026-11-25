#!/usr/bin/env python3
"""Figura: 15 metricas concretas mais reportadas, split academico vs cinza.

Le data/master/metric_inventory.csv (gerado por metric_inventory.py) e
escreve latex-article/figures/fig_metric_inventory.png/.pdf.
"""
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
INV = ROOT / 'data' / 'master' / 'metric_inventory.csv'
FIGS = ROOT / 'latex-article' / 'figures'
STATS = ROOT / 'data' / 'master' / 'mlr_stats.json'  # corpus sizes for the legend

LBL = {'ProdPerf': 'Productivity/Perf.', 'SurveyPerc': 'Survey/Percept.',
       'Satisf': 'Satisfaction', 'Collab': 'Collaboration',
       'Quality': 'Quality', 'Activity': 'Activity/Code',
       'Agile': 'Agile/Process', 'Delivery': 'Delivery',
       'DevExDim': 'DevEx Dim.'}
NAME = {'productivity / efficiency score': 'Productivity/efficiency score',
        'task / contribution throughput': 'Task/contribution throughput',
        'perceived productivity (self-report)': 'Perceived productivity (self-report)',
        'flow state / focus time': 'Flow state/focus time',
        'lines of code changed': 'Lines of code changed',
        'change failure rate': 'Change failure rate',
        'defects / rollbacks': 'Defects/rollbacks',
        'mean time to restore': 'Mean time to restore',
        'code quality / health': 'Code quality/health',
        'deployment frequency': 'Deployment frequency',
        'lead time for changes': 'Lead time for changes',
        'satisfaction': 'Developer satisfaction',
        'performance rating': 'Performance rating',
        'activity counts (generic)': 'Activity counts (generic)',
        'code-review interaction': 'Code-review interaction',
        'task completion time': 'Task completion time',
        'commit count': 'Commit count',
        'engagement / motivation / retention': 'Engagement/motivation/retention',
        'AI suggestion acceptance / persistence': 'AI suggestion acceptance/persistence',
        'pull-request count / time': 'Pull-request count/time',
        'cycle time': 'Cycle time',
        'survey / psychometric instrument': 'Survey/psychometric instrument',
        'cognitive load': 'Cognitive load',
        'collaboration / knowledge sharing': 'Collaboration/knowledge sharing'}


def main():
    rows = [r for r in list(csv.reader(open(INV)))[1:]
            if not r[0].startswith('OTHER')]
    rows.sort(key=lambda r: -int(r[2]))
    top = rows[:15][::-1]  # barh de baixo p/ cima

    labels = [f"{NAME.get(r[1], r[1])}  [{LBL[r[0]]}]" for r in top]
    acad = [int(r[3]) for r in top]
    grey = [int(r[4]) for r in top]

    corpus = {'academic_included': 153, 'grey_included': 75}  # D1 recount 2026-10-19 (228 sources)
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    y = range(len(top))
    ax.barh(y, acad, color='#1f77b4', edgecolor='white', height=0.68,
            label=f"Academic (n={corpus['academic_included']})")
    ax.barh(y, grey, left=acad, color='#c8aa5a', edgecolor='white',
            height=0.68, label=f"Gray (n={corpus['grey_included']})")
    for i, (a, g) in enumerate(zip(acad, grey)):
        # counts of each segment (advisor comment: academic and gray values on every bar)
        if a >= 3:
            ax.text(a / 2, i, str(a), va='center', ha='center', fontsize=8, color='white')
        if g >= 3:
            ax.text(a + g / 2, i, str(g), va='center', ha='center', fontsize=8, color='#222')
        ax.text(a + g + 0.4, i, str(a + g), va='center', fontsize=9,
                color='#222', fontweight='bold')
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel('Number of sources', fontsize=10)
    ax.set_xlim(0, max(a + g for a, g in zip(acad, grey)) + 3)
    ax.xaxis.grid(True, color='#dddddd', linewidth=0.6)
    ax.set_axisbelow(True)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.legend(loc='lower right', fontsize=9, frameon=False)
    fig.tight_layout()
    FIGS.mkdir(exist_ok=True)
    fig.savefig(FIGS / 'fig_metric_inventory.png', dpi=300)
    fig.savefig(FIGS / 'fig_metric_inventory.pdf')
    print('ok', FIGS / 'fig_metric_inventory.png')


if __name__ == '__main__':
    main()
