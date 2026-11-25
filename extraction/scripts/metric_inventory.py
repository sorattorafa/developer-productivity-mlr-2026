#!/usr/bin/env python3
"""Inventory of the concrete metrics reported by each source (metrics part of RQ1).

Pipeline: (1) harvest of the metric tables of the NotebookLM summaries
(format `| Metrica | Categoria | Nivel | Como Coletada | Validada |` and
`## Metricas Mencionadas` lists, as written by the extractor); (2) normalization by ordered rules
into canonical names and the 9 categories of the codebook; (3) manual supplement
for 10 sources without a usable summary (State of DevOps reports, etc.;
justification in the MANUAL dictionary); (4) aggregation by unique sources.

Some patterns and keys below are in Portuguese because they match the raw extractor outputs.

Outputs:
  data/master/metric_inventory.csv               aggregated inventory
  data/master/metric_inventory_unclassified.csv  unclassified residue
  data/master/metric_inventory_nonmetric.csv     excluded items (non-metrics)

Sources reclassified from academic to gray keep their summary under the original
ID P#### (G2P map).
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
NLM = ROOT / 'extraction' / 'notebooklm'
OUT = ROOT / 'data' / 'master'
MASTER = OUT / 'MLR_Final_Consolidated.xlsx'


def corpus_ids():
    """IDs of the final corpus (sources with an Include verdict in the master)."""
    wb = openpyxl.load_workbook(MASTER, read_only=True)
    ids = set()
    for sheet, vcol in (('Included Papers', 30), ('Grey Literature', 19)):
        for r in list(wb[sheet].iter_rows(values_only=True))[1:]:
            if r[0] and r[vcol] and 'include' in str(r[vcol]).lower():
                ids.add(str(r[0]).strip())
    return ids

G2P = {'G073': 'P_NEW_1', 'G074': 'P1274', 'G075': 'P1295', 'G076': 'P1354',
       'G077': 'P1357', 'G078': 'P1365', 'G079': 'P1420', 'G080': 'P1437'}

TABLE_RX = re.compile(r'\|\s*M[ée]tric[ao]\s*\|[^\n]*\n\|[-| ]+\n((?:\|[^\n]*\n)+)')
BULLET_SEC = re.compile(r'##\s*M[ée]tricas? Mencionadas(.*?)(?:\n##|\Z)', re.S)
BULLET_RX = re.compile(r'[*-]\s+\*\*(.+?)\*\*')


def harvest():
    rows = []
    for f in sorted(NLM.glob('*_notebooklm.md')):
        sid = f.name.split('_')[0]
        text = f.read_text(errors='ignore')
        got = False
        for m in TABLE_RX.finditer(text):
            for line in m.group(1).strip().split('\n'):
                cells = [c.strip() for c in line.strip('|').split('|')]
                if cells and cells[0] and cells[0].lower() not in ('metrica', 'métrica', '---'):
                    rows.append((sid, cells[0]))
                    got = True
        if not got:
            for sec in BULLET_SEC.finditer(text):
                for b in BULLET_RX.finditer(sec.group(1)):
                    rows.append((sid, b.group(1)))
    # remap summaries stored under the original P IDs to the final G IDs and filter by the corpus
    p2g = {v: k for k, v in G2P.items()}
    keep = corpus_ids()
    return [(p2g.get(sid, sid), raw) for sid, raw in rows
            if p2g.get(sid, sid) in keep]


def clean(n):
    n = re.sub(r'\*\*|\*|`', '', n)
    n = re.sub(r'\s*\([A-Z]{2,6}\)\s*$', '', n)
    return re.sub(r'\s+', ' ', n).strip(' .:;').lower()


# items that are not productivity metrics (analysis methods, factors,
# study context); excluded and logged
NONMETRIC = re.compile(
    r'grounded theory|qualitative codes|inter-coder|word frequency|'
    r'frequency of expectation|48 productivity factors|estrat[ée]gias|'
    r'social welfare|price-of|threshold completed|deployment environment|'
    r'project status|probability bias|cost bias|agreement level|'
    r'team formation|relevance of solutions|'
    # generic category labels, not individual metrics
    r'^devops metrics$|^key metrics$|^engineering metrics$|'
    r'^system metrics$|^outras$|^measurement approaches$|'
    r'^multi-dimensional metrics$|-level metrics$|^lifecycle metrics$|'
    r'^productivity & ci/cd$|^ai impact|^m[ée]tricas de resultados|'
    r'^measures of high-performing|^time-based measures|'
    r'^developer experience, product excellence|'
    r'^speed$|^effectiveness$|^quality$|formul[áa]rio de extra|'
    r's[íi]ntese de dados')

# ordered rules: (regex, canonical name, category)
RULES = [
    # Delivery
    (r'deploy(ment)? frequen', 'deployment frequency', 'Delivery'),
    (r'lead time', 'lead time for changes', 'Delivery'),
    (r'cycle time|time-in-development', 'cycle time', 'Delivery'),
    (r'time to market|release (frequen|count)|delivery (speed|performance|rate)|deploys? per|deployment (count|time)\b|at sign-off', 'release frequency / time to market', 'Delivery'),
    (r'^dora metrics$|four key', 'DORA metrics (composite)', 'Delivery'),
    # Quality
    (r'change fail|failed deployment', 'change failure rate', 'Quality'),
    (r'mttr|mean time to (restore|recover|repair)|time to restore|recovery time', 'mean time to restore', 'Quality'),
    (r'defect|bug (count|rate|density)|bugs?\b|escape|rollback|fix rate', 'defects / rollbacks', 'Quality'),
    (r'test coverage|code coverage|test (pass|success)|flakiness|pass rate|test case duration', 'test outcomes (coverage, flakiness)', 'Quality'),
    (r'code quality|quality (score|of code|gate)|maintainab|code health|code smell|vulnerab|security', 'code quality / health', 'Quality'),
    (r'incident|instabilit|reliabilit|outage|availability|uptime', 'incidents / instability', 'Quality'),
    (r'rework|technical debt|refactor|td (types|introduction)|negative impact of td', 'rework / technical debt', 'Quality'),
    (r'buildsuccess|build (success|failure)', 'build success rate', 'Quality'),
    # Activity
    (r'commit', 'commit count', 'Activity'),
    (r'pull request|\bpr\b|merge (rate|frequency|count)|prs\b|totalpullrequest', 'pull-request count / time', 'Activity'),
    (r'lines of code|\bloc\b|code volume|lines? (changed|added|inserted|deleted)|line (inserted|deleted)|files modified|change size', 'lines of code changed', 'Activity'),
    (r'churn', 'code churn', 'Activity'),
    (r'diffs|changelist|check-?ins?|edits|keystrokes|ide (event|interaction)|compile count|job status|execution (path|delta)|exception frequency|question (count|view)|emails sent|application windows|inbox size|websites visited|applications used', 'fine-grained activity events', 'Activity'),
    (r'build (count|frequency|time)|builds\b|number of builds|buildtime|build importance', 'build count / time', 'Activity'),
    (r'accept(ance)? (rate|frequency)|suggestion.*accept|persistence rate|code retention', 'AI suggestion acceptance / persistence', 'Activity'),
    (r'prompting / validation', 'AI verification time', 'Activity'),
    (r'hours (worked|active)|net time|inactive periods|time \(hours', 'work hours / active time', 'Activity'),
    (r'activity\b|actv|extra activities|tasks worked on|occurrence/frequency', 'activity counts (generic)', 'Activity'),
    # ProdPerf
    (r'velocit', 'velocity', 'ProdPerf'),
    (r'story point', 'story points completed', 'ProdPerf'),
    (r'throughput|tasks? (complet|deliver|per)|issues? (closed|resolved)|features? (deliver|shipped)|work items|contribution (speed|analysis|count)', 'task / contribution throughput', 'ProdPerf'),
    (r'productivity (score|index|metric|gain|rate)|efficiency|engineering efficiency|^(average )?productivity$|fair developer score|output|active score|stability score', 'productivity / efficiency score', 'ProdPerf'),
    (r'time (sav|spent)|task (time|completion|duration)|coding (time|effort)|development time|dwelltime|processing time', 'task completion time', 'ProdPerf'),
    (r'effort|fte|cosmic function|function point|cocomo|size estimat', 'effort / size estimates', 'ProdPerf'),
    (r'(file|annotation) accuracy|success \(correctness\)', 'task correctness (experiments)', 'ProdPerf'),
    (r'performance\b|perf\b|job performance|goal (attain|achiev)|self-appraisal', 'performance rating', 'ProdPerf'),
    # SurveyPerc
    (r'self-?(rated|reported|assessed)|perceived (productiv|efficien|effect|useful)', 'perceived productivity (self-report)', 'SurveyPerc'),
    (r'likert|survey|questionn|experience sampling|diary|system usability|\bsus\b|utaut|tam\b', 'survey / psychometric instrument', 'SurveyPerc'),
    (r'workload|task load|nasa', 'perceived workload', 'SurveyPerc'),
    (r'eeg|biometric|physiolog|heart rate|skin conduct|eye track|fixation|corsi', 'physiological / cognition measures', 'SurveyPerc'),
    (r'dexi|attrakdiff|sad-2|oux|overall ux|need fulfillment|\bnfs\b', 'experience scales (DEXI, AttrakDiff)', 'SurveyPerc'),
    (r'ease of use|learnability|perceived (challenge|simplicity)|documentation adequacy|initial perceptions|effectiveness \(user|interesse|inten[çc]', 'perceived usability / learnability', 'SurveyPerc'),
    (r'understanding time|navigation time|scope understanding', 'comprehension tasks', 'SurveyPerc'),
    # Satisf
    (r'satisfa|satf', 'satisfaction', 'Satisf'),
    (r'well-?being|wellness', 'well-being', 'Satisf'),
    (r'burnout|stress|fatigue|exhaust|frustration|bad day', 'burnout / stress / frustration', 'Satisf'),
    (r'happiness|unhappiness|affect|emotion|panas|\bsam\b|mood|senti(ment|strength)|spane|positive and negative experience|arousal|dominance', 'affect / sentiment', 'Satisf'),
    (r'engagement|motivation|\bimi\b|enps|morale|retention|turnover|attrition|intention to (stay|leave)', 'engagement / motivation / retention', 'Satisf'),
    (r'cips|self compassion|s-scs|anxiety self', 'psychometric scales (CIPS, S-SCS)', 'Satisf'),
    # Collab
    (r'communicat|comm\b', 'communication frequency / quality', 'Collab'),
    (r'code.?review|review (turnaround|time|latency|participation|comments?|count)|peer review|totalreviewers|time-to-(merge|first-response|accept)', 'code-review interaction', 'Collab'),
    (r'collaborat|knowledge (shar|transfer)|coordination|cohesion|social (network|coding)|sna |betweenness|pair|dependency on colleagues|distinct authors|code ownership|graph-based', 'collaboration / knowledge sharing', 'Collab'),
    (r'meeting', 'meeting load', 'Collab'),
    (r'onboarding|ramp-?up|mentor', 'onboarding / mentoring', 'Collab'),
    # DevExDim
    (r'flow state|\bflow\b|immersion|deep work|focus|uninterrupted', 'flow state / focus time', 'DevExDim'),
    (r'cognitive load|mental (load|effort)|carga cognitiva', 'cognitive load', 'DevExDim'),
    (r'feedback loop|feedback (time|speed)|ci wait|wait(ing)? time', 'feedback loops', 'DevExDim'),
    (r'context switch|interrupt|work fragmentation|misalignment|disturbance level', 'interruptions / context switches', 'DevExDim'),
    (r'developer experience index|\bdxi\b|devex|dx (score|index)|effc|compliance interaction|toolchain efficiency', 'experience indices (DXI, rSPACE)', 'DevExDim'),
    # Agile
    (r'sprint|burn-?down|iteration|kanban|\bwip\b|cumulative flow|backlog|planning accuracy|estimation accuracy|scope creep', 'sprint / iteration metrics', 'Agile'),
    (r'inner.?/?.?outer loop|inner loop|engineer time allocation', 'inner/outer-loop time', 'Agile'),
    # outside the 9 categories
    (r'pass@k|bleu|rouge|meteor|f1-score|^(accuracy|precision|recall)$|kappa', 'model-evaluation metrics', 'OTHER-modeleval'),
    (r'halstead|complexity', 'code size / complexity', 'OTHER-codelevel'),
    (r'customer|csat|nps\b|business|revenue|market|user (growth|adoption)', 'business/customer metrics', 'OTHER-business'),
    (r'talent|capabilit|skill|knowledge, skills|seniority|experience level|expertise|years of|project (experience|size)', 'people/capability descriptors', 'OTHER-people'),
    (r'\(x\d+\)|autonomy|clarity|psychological safety|culture|task (visibility|predictability)', 'factors (not metrics)', 'OTHER-factor'),
]

# curated mapping of the tail (exact names after clean); reviewed manually
CURATED = {
    'métricas de desempenho de entrega de software (métricas dora)': ('DORA metrics (composite)', 'Delivery'),
    'dora quick check assessment': ('DORA metrics (composite)', 'Delivery'),
    'new issues (lifecycle metrics)': ('activity counts (generic)', 'Activity'),
    'deploys (lifecycle metrics)': ('deployment frequency', 'Delivery'),
    'stage durations': ('cycle time', 'Delivery'),
    'shown rate': ('AI suggestion acceptance / persistence', 'Activity'),
    'total volume': ('AI suggestion acceptance / persistence', 'Activity'),
    'loquaciousness': ('AI suggestion acceptance / persistence', 'Activity'),
    'eagerness': ('AI suggestion acceptance / persistence', 'Activity'),
    'developer speed': ('productivity / efficiency score', 'ProdPerf'),
    'adoption metrics': ('tool adoption rate', 'Activity'),
    'adoption rate': ('tool adoption rate', 'Activity'),
    'uso de ia para geração de código': ('tool adoption rate', 'Activity'),
    'enablement metrics': ('tool adoption rate', 'Activity'),
    'feature value': ('business/customer metrics', 'OTHER-business'),
    'pickup time (leading indicator)': ('code-review interaction', 'Collab'),
    'engineering investment allocation': ('business/customer metrics', 'OTHER-business'),
    'resource allocation': ('business/customer metrics', 'OTHER-business'),
    'accuracy scores': ('task correctness (experiments)', 'ProdPerf'),
    'meaningful contributions': ('task / contribution throughput', 'ProdPerf'),
    'consistency': ('productivity / efficiency score', 'ProdPerf'),
    'balancing new value and maintenance': ('work-mix balance (planned vs unplanned)', 'Agile'),
    'task balance': ('work-mix balance (planned vs unplanned)', 'Agile'),
    'unplanned and added work': ('work-mix balance (planned vs unplanned)', 'Agile'),
    'frequency of unplanned tasks': ('work-mix balance (planned vs unplanned)', 'Agile'),
    'knowledge expansion': ('learning / growth', 'DevExDim'),
    'learning acceleration': ('learning / growth', 'DevExDim'),
    'learning and creativity': ('learning / growth', 'DevExDim'),
    'creativity': ('learning / growth', 'DevExDim'),
    'codebase navigability': ('DevEx driver items (survey)', 'DevExDim'),
    'ease of doing work': ('DevEx driver items (survey)', 'DevExDim'),
    'ci/cd tooling ease': ('DevEx driver items (survey)', 'DevExDim'),
    'specification quality': ('DevEx driver items (survey)', 'DevExDim'),
    'frequency of feeling productive': ('perceived productivity (self-report)', 'SurveyPerc'),
    'validate local code change': ('feedback loops', 'DevExDim'),
    'validate component integration': ('feedback loops', 'DevExDim'),
    'validate non-functional requirements': ('feedback loops', 'DevExDim'),
    'become productive on new team': ('onboarding / mentoring', 'Collab'),
    'get answers to internal technical query': ('DevEx driver items (survey)', 'DevExDim'),
    'launch new service in production': ('feedback loops', 'DevExDim'),
    'employee experience scores': ('experience scales (DEXI, AttrakDiff)', 'SurveyPerc'),
    'e-factor': ('flow state / focus time', 'DevExDim'),
    'completion time (s)': ('task completion time', 'ProdPerf'),
    'forecasted speedup': ('productivity / efficiency score', 'ProdPerf'),
    'prior task exposure & external resource needs': ('people/capability descriptors', 'OTHER-people'),
    'build induced latency': ('feedback loops', 'DevExDim'),
    'co-pilot assistance metrics': ('AI suggestion acceptance / persistence', 'Activity'),
    'stability / user crash rate': ('incidents / instability', 'Quality'),
    'main fail rate (dora-aligned)': ('change failure rate', 'Quality'),
    'average turnaround time': ('cycle time', 'Delivery'),
    'automation health': ('code quality / health', 'Quality'),
    'mau (monthly active users) & rmau': ('business/customer metrics', 'OTHER-business'),
    'social translucence': ('collaboration / knowledge sharing', 'Collab'),
    'accepted lines-of-code': ('AI suggestion acceptance / persistence', 'Activity'),
    'productivity increase': ('productivity / efficiency score', 'ProdPerf'),
    'support ticket volume': ('incidents / instability', 'Quality'),
    'dat (diff authoring time)': ('task completion time', 'ProdPerf'),
    'size-related metrics (ex: source code)': ('code size / complexity', 'OTHER-codelevel'),
    'function-related metrics': ('effort / size estimates', 'ProdPerf'),
    'code protection (coverage)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'ease of understanding documentation': ('DevEx driver items (survey)', 'DevExDim'),
    'time to generate ci results': ('feedback loops', 'DevExDim'),
    'manual steps to deploy': ('DevEx driver items (survey)', 'DevExDim'),
    'time to first hello, world': ('onboarding / mentoring', 'Collab'),
    'work-life balance': ('well-being', 'Satisf'),
    'wasted time (tempo desperdiçado)': ('task completion time', 'ProdPerf'),
    'quality of work': ('code quality / health', 'Quality'),
    'speed (perceived)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'self-efficacy': ('psychometric scales (CIPS, S-SCS)', 'Satisf'),
    'chat response speed': ('communication frequency / quality', 'Collab'),
    'kloc / sloc': ('effort / size estimates', 'ProdPerf'),
    'use case points': ('effort / size estimates', 'ProdPerf'),
    'star ratings': ('business/customer metrics', 'OTHER-business'),
    'downloads': ('business/customer metrics', 'OTHER-business'),
    'ratings/reviews': ('business/customer metrics', 'OTHER-business'),
    'fixed issue time': ('defects / rollbacks', 'Quality'),
    'tempo pesquisando respostas': ('DevEx driver items (survey)', 'DevExDim'),
    'experiência do desenvolvedor': ('experience indices (DXI, rSPACE)', 'DevExDim'),
    'número de linguagens utilizadas': ('people/capability descriptors', 'OTHER-people'),
    'engaging tasks': ('engagement / motivation / retention', 'Satisf'),
    'time to get questions answered': ('DevEx driver items (survey)', 'DevExDim'),
    'ease of deploying changes': ('DevEx driver items (survey)', 'DevExDim'),
    'ease of understanding code': ('DevEx driver items (survey)', 'DevExDim'),
    'intuitiveness of processes': ('DevEx driver items (survey)', 'DevExDim'),
    'intuitiveness of tools': ('DevEx driver items (survey)', 'DevExDim'),
    'sense of accomplishment': ('satisfaction', 'Satisf'),
    'readability': ('code quality / health', 'Quality'),
    'character length': ('code size / complexity', 'OTHER-codelevel'),
    'familiarity with code completion': ('people/capability descriptors', 'OTHER-people'),
    'total cost of build': ('business/customer metrics', 'OTHER-business'),
    'impact / value': ('business/customer metrics', 'OTHER-business'),
    'perceived change in team productivity': ('perceived productivity (self-report)', 'SurveyPerc'),
    'ability to reach milestones': ('performance rating', 'ProdPerf'),
    'social connection with team members': ('collaboration / knowledge sharing', 'Collab'),
    'frequency of scheduled social activities': ('collaboration / knowledge sharing', 'Collab'),
    "awareness of colleague's work": ('collaboration / knowledge sharing', 'Collab'),
    'software productivity': ('productivity / efficiency score', 'ProdPerf'),
    'team empowerment': ('factors (not metrics)', 'OTHER-factor'),
    'quality conformance (testing)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'environment and workflow': ('factors (not metrics)', 'OTHER-factor'),
    'perception of factors': ('factors (not metrics)', 'OTHER-factor'),
}

# sources without a usable summary; metrics confirmed by targeted reading
# of the PDFs or pages (DORA reports use the four metrics by definition)
MANUAL = {
    # G004/G008: State of DevOps reports (DORA); they operationalize the
    # four key metrics by definition (full text unavailable)
    'G004': [('deployment frequency', 'Delivery'), ('lead time for changes', 'Delivery'), ('change failure rate', 'Quality'), ('mean time to restore', 'Quality')],
    'G008': [('deployment frequency', 'Delivery'), ('lead time for changes', 'Delivery'), ('change failure rate', 'Quality'), ('mean time to restore', 'Quality')],
    # G073: comparison of DORA/SPACE/HEART/AARRR (NotebookLM summary)
    'G073': [('DORA metrics (composite)', 'Delivery'), ('experience indices (DXI, rSPACE)', 'DevExDim'), ('business/customer metrics', 'OTHER-business')],
    # G026: full text unavailable; P1286: reports no concrete
    # metrics (rapid review on DX in reuse); no entry for either
    'G005': [('deployment frequency', 'Delivery'), ('lead time for changes', 'Delivery'), ('change failure rate', 'Quality'), ('mean time to restore', 'Quality')],
    'G006': [('deployment frequency', 'Delivery'), ('lead time for changes', 'Delivery'), ('change failure rate', 'Quality'), ('mean time to restore', 'Quality')],
    'G007': [('deployment frequency', 'Delivery'), ('lead time for changes', 'Delivery'), ('change failure rate', 'Quality'), ('mean time to restore', 'Quality')],
    'G009': [('deployment frequency', 'Delivery'), ('incidents / instability', 'Quality'), ('task / contribution throughput', 'ProdPerf'), ('AI suggestion acceptance / persistence', 'Activity')],
    'G019': [('cycle time', 'Delivery'), ('pull-request count / time', 'Activity'), ('deployment frequency', 'Delivery'), ('code-review interaction', 'Collab')],
    'G025': [('experience indices (DXI, rSPACE)', 'DevExDim'), ('deployment frequency', 'Delivery'), ('satisfaction', 'Satisf')],
    'G033': [('feedback loops', 'DevExDim'), ('cognitive load', 'DevExDim'), ('flow state / focus time', 'DevExDim')],
    'G036': [('task / contribution throughput', 'ProdPerf'), ('incidents / instability', 'Quality'), ('deployment frequency', 'Delivery')],
    'G048': [('deployment frequency', 'Delivery'), ('satisfaction', 'Satisf'), ('cycle time', 'Delivery')],
    'G049': [('experience indices (DXI, rSPACE)', 'DevExDim'), ('deployment frequency', 'Delivery'), ('satisfaction', 'Satisf')],
}


# Search update 2026-10: names from the 99 new sources that no rule covered,
# mapped on 2026-10-19 (assistant draft, reviewed by the author). Same criterion as CURATED.
CURATED_UPDATE = {
    '0 to 200': ('onboarding / mentoring', 'Collab'),
    'absenteeism': ('engagement / motivation / retention', 'Satisf'),
    'access labor / time on sighted help & diy': ('task completion time', 'ProdPerf'),
    'accessibility (acessibilidade)': ('code quality / health', 'Quality'),
    'active coding share of workweek (houck et al., idc, atlassian)': ('inner/outer-loop time', 'Agile'),
    'active rejection rate (taxa de rejeição ativa)': ('AI suggestion acceptance / persistence', 'Activity'),
    'active screen time / idle time': ('work hours / active time', 'Activity'),
    'adjusted suggestion verification time [19-21]': ('AI verification time', 'Activity'),
    'ai assistance adoption rate': ('tool adoption rate', 'Activity'),
    'ai perception': ('trust in AI tools', 'SurveyPerc'),
    'ai trust / perceived usability': ('trust in AI tools', 'SurveyPerc'),
    'ai usage telemetry (tokens used, lines accepted, usage cost, intervention dates)': ('tool adoption rate', 'Activity'),
    'ai-generated code adoption rate': ('AI suggestion acceptance / persistence', 'Activity'),
    'alert false positive rate': ('model-evaluation metrics', 'OTHER-modeleval'),
    'anchor-dat': ('task completion time', 'ProdPerf'),
    'anos de experiência': ('people/capability descriptors', 'OTHER-people'),
    'app store & google play store releases': ('release frequency / time to market', 'Delivery'),
    'appeal, design & aesthetics': ('experience scales (DEXI, AttrakDiff)', 'SurveyPerc'),
    'application of previous knowledge': ('learning / growth', 'DevExDim'),
    'applik (liking - approach)': ('affect / sentiment', 'Satisf'),
    'apppls (pleasure - approach)': ('affect / sentiment', 'Satisf'),
    'artificial intelligence': ('factors (not metrics)', 'OTHER-factor'),
    'attractive implementation tasks': ('engagement / motivation / retention', 'Satisf'),
    'aumento de produtividade e velocidade (leverage / speed)': ('productivity / efficiency score', 'ProdPerf'),
    'autocomplete tools (e.g., github copilot)': ('commit count', 'Activity'),
    "autocorrelation metrics (gini index & cramer's v) (candidates)": ('work hours / active time', 'Activity'),
    'automated report adoption rate': ('tool adoption rate', 'Activity'),
    'autonomous asynchronous agents': ('commit count', 'Activity'),
    'average snippet size (browser / ai / total)': ('code size / complexity', 'OTHER-codelevel'),
    'backward digit span score': ('physiological / cognition measures', 'SurveyPerc'),
    'behavioral intention': ('perceived usability / learnability', 'SurveyPerc'),
    'big five personality traits (agreeableness, neuroticism, intellect/openness, extraversion, conscientiousness)': ('people/capability descriptors', 'OTHER-people'),
    "blau's diversity index": ('people/capability descriptors', 'OTHER-people'),
    'blocked submission attempts / ci failures': ('build success rate', 'Quality'),
    'build latency': ('feedback loops', 'DevExDim'),
    'build speed': ('feedback loops', 'DevExDim'),
    'cache hit rate': ('model-evaluation metrics', 'OTHER-modeleval'),
    'cadência de entrega e fluxo': ('release frequency / time to market', 'Delivery'),
    'carga de revisão de código': ('code-review interaction', 'Collab'),
    'change count': ('commit count', 'Activity'),
    'changes submitted / code delivered': ('task / contribution throughput', 'ProdPerf'),
    'chrf score': ('model-evaluation metrics', 'OTHER-modeleval'),
    'client-perceived quality / qualidade percebida pelo cliente': ('business/customer metrics', 'OTHER-business'),
    'cobertura de verificação de privacidade automática': ('test outcomes (coverage, flakiness)', 'Quality'),
    'code correctness / functional accuracy': ('task correctness (experiments)', 'ProdPerf'),
    'code functionality': ('code quality / health', 'Quality'),
    'code gestation time': ('cycle time', 'Delivery'),
    'code optimization': ('code quality / health', 'Quality'),
    'code readability': ('code quality / health', 'Quality'),
    'code reusability': ('code quality / health', 'Quality'),
    'code reuse': ('code quality / health', 'Quality'),
    'code suggestion accuracy rate': ('AI suggestion acceptance / persistence', 'Activity'),
    'code understanding': ('DevEx driver items (survey)', 'DevExDim'),
    'code_comprehensibility': ('DevEx driver items (survey)', 'DevExDim'),
    'code_identifiability': ('DevEx driver items (survey)', 'DevExDim'),
    'codehealth': ('code quality / health', 'Quality'),
    'coding days per week': ('work hours / active time', 'Activity'),
    'cognition (dx dimension: técnicas, plataformas, processos, habilidades) [17]': ('DevEx driver items (survey)', 'DevExDim'),
    'collective self-esteem / cse (public cse, membership esteem, private cse, importance to identity)': ('psychometric scales (CIPS, S-SCS)', 'Satisf'),
    'comment line density': ('code quality / health', 'Quality'),
    'commercial/oss development experience (sq10)': ('people/capability descriptors', 'OTHER-people'),
    'comparative experience vs. enterprise search (q13)': ('perceived usability / learnability', 'SurveyPerc'),
    'compilation error rate': ('defects / rollbacks', 'Quality'),
    'completed tasks volume': ('task / contribution throughput', 'ProdPerf'),
    'completion time': ('task completion time', 'ProdPerf'),
    'computer self-efficacy': ('psychometric scales (CIPS, S-SCS)', 'Satisf'),
    'conation (dx dimension: objetivos, alinhamento, motivação, compromisso) [17]': ('engagement / motivation / retention', 'Satisf'),
    'confianca no codigo gerado por ai': ('trust in AI tools', 'SurveyPerc'),
    'consistent code style': ('code quality / health', 'Quality'),
    'contagem de testes automatizados': ('test outcomes (coverage, flakiness)', 'Quality'),
    'continuous integration hindrance rating (sq4.5)': ('DevEx driver items (survey)', 'DevExDim'),
    'convergence entropy (\\\\(h_{conv}\\\\))': ('collaboration / knowledge sharing', 'Collab'),
    'copilot evaluation score': ('perceived productivity (self-report)', 'SurveyPerc'),
    'copilot is valuable ("i view copilot as a valuable tool for developers") [8, 9]': ('perceived productivity (self-report)', 'SurveyPerc'),
    'correct syntax importance': ('code quality / health', 'Quality'),
    'correctness, consistency, comprehensiveness, conciseness': ('model-evaluation metrics', 'OTHER-modeleval'),
    'cost & roi metrics': ('business/customer metrics', 'OTHER-business'),
    'counterfactual stickiness (q12)': ('perceived usability / learnability', 'SurveyPerc'),
    'cpu, memory & infrastructure utilization': ('incidents / instability', 'Quality'),
    'critical of ai in public sector ("i am critical of the use of ai-tools in the public sector") [8, 9, 13]': ('trust in AI tools', 'SurveyPerc'),
    'cups state dwell time (% session time) [5, 13, 17]': ('AI verification time', 'Activity'),
    'debugging instances': ('fine-grained activity events', 'Activity'),
    'degree centrality': ('collaboration / knowledge sharing', 'Collab'),
    'degree-of-interest (doi) / working set': ('fine-grained activity events', 'Activity'),
    'deletion rate (taxa de deleção de código pós-interrupção)': ('fine-grained activity events', 'Activity'),
    'deletions': ('fine-grained activity events', 'Activity'),
    'delivery consistency': ('release frequency / time to market', 'Delivery'),
    'dependent on colleagues ("i am dependent on colleagues for help and guidance") [8, 9, 13]': ('collaboration / knowledge sharing', 'Collab'),
    'developer friction': ('experience indices (DXI, rSPACE)', 'DevExDim'),
    'developer productivity': ('perceived productivity (self-report)', 'SurveyPerc'),
    'developer productivity loss rating (sq4.3)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'developer self-efficacy': ('psychometric scales (CIPS, S-SCS)', 'Satisf'),
    'developer thriving scale': ('psychometric scales (CIPS, S-SCS)', 'Satisf'),
    'diagnostics density': ('code quality / health', 'Quality'),
    'diff authoring time': ('task completion time', 'ProdPerf'),
    'diversificacao de ferramentas de ai': ('tool adoption rate', 'Activity'),
    'documentation / process improvement [9]': ('activity counts (generic)', 'Activity'),
    'documentation quality & accessibility': ('DevEx driver items (survey)', 'DevExDim'),
    'documentation quality & volume': ('code quality / health', 'Quality'),
    'documentation searchability': ('DevEx driver items (survey)', 'DevExDim'),
    'documentation writing quality': ('code quality / health', 'Quality'),
    'duplicate line density': ('code quality / health', 'Quality'),
    'duplicated code': ('code quality / health', 'Quality'),
    'duplicated line density': ('code quality / health', 'Quality'),
    'duration': ('effort / size estimates', 'ProdPerf'),
    'dwell time (tempo de olhar/fixação na sugestão)': ('physiological / cognition measures', 'SurveyPerc'),
    'ease (e)': ('DevEx driver items (survey)', 'DevExDim'),
    'edit lag': ('interruptions / context switches', 'DevExDim'),
    'edit ratio': ('fine-grained activity events', 'Activity'),
    'edited documents count': ('fine-grained activity events', 'Activity'),
    'effectiveness (eficácia)': ('task correctness (experiments)', 'ProdPerf'),
    'effectiveness strategies': ('factors (not metrics)', 'OTHER-factor'),
    'error fix time': ('defects / rollbacks', 'Quality'),
    'erros de compilacao e defeitos semanticos': ('defects / rollbacks', 'Quality'),
    'escore de equilibrio criacao-verificacao (balance score)': ('AI verification time', 'Activity'),
    'estatísticas de uso de fornecedores de ia (ai vendor usage stats)': ('tool adoption rate', 'Activity'),
    'estimation adherence & delays': ('sprint / iteration metrics', 'Agile'),
    'expectations fulfillment': ('performance rating', 'ProdPerf'),
    'explicit dev-process rules': ('factors (not metrics)', 'OTHER-factor'),
    'explicit test rules': ('factors (not metrics)', 'OTHER-factor'),
    'exploitation and exploration tensions': ('factors (not metrics)', 'OTHER-factor'),
    'external pastes': ('fine-grained activity events', 'Activity'),
    'eye blinks': ('physiological / cognition measures', 'SurveyPerc'),
    'feature completeness': ('perceived usability / learnability', 'SurveyPerc'),
    'feedback quality': ('feedback loops', 'DevExDim'),
    'file switching frequency': ('interruptions / context switches', 'DevExDim'),
    'first-try policy compliance (q9)': ('code quality / health', 'Quality'),
    'fixing time by generation time ratio': ('AI verification time', 'Activity'),
    'flaky test action frequency ratings (sq7.1–sq7.8)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'flaky test cause frequency ratings (sq5.1–sq5.10)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'flaky test failure reproduction difficulty (sq4.7)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'flaky test observation frequency (sq3)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'flaky tests frequency': ('test outcomes (coverage, flakiness)', 'Quality'),
    'fork entropy': ('collaboration / knowledge sharing', 'Collab'),
    'forward digit span score': ('physiological / cognition measures', 'SurveyPerc'),
    'fraction of code written by ml': ('AI suggestion acceptance / persistence', 'Activity'),
    'frequencia de migracao de esquema de banco de dados': ('code churn', 'Activity'),
    'frequencia de uso diario': ('tool adoption rate', 'Activity'),
    'frequency of seeking external help': ('interruptions / context switches', 'DevExDim'),
    'friction & productivity hindrances': ('DevEx driver items (survey)', 'DevExDim'),
    'friction / atrito de desenvolvimento': ('DevEx driver items (survey)', 'DevExDim'),
    'functional value': ('perceived productivity (self-report)', 'SurveyPerc'),
    'future usage preference': ('perceived usability / learnability', 'SurveyPerc'),
    'ganho de produtividade percebido': ('perceived productivity (self-report)', 'SurveyPerc'),
    'genai usage': ('tool adoption rate', 'Activity'),
    'genai usage frequency': ('tool adoption rate', 'Activity'),
    'goal importance': ('factors (not metrics)', 'OTHER-factor'),
    'goal maintenance': ('flow state / focus time', 'DevExDim'),
    'healthy metrics use': ('factors (not metrics)', 'OTHER-factor'),
    'heavy ai usage rate': ('tool adoption rate', 'Activity'),
    'helpfulness': ('perceived productivity (self-report)', 'SurveyPerc'),
    'hindrance by changing/unclear requirements': ('DevEx driver items (survey)', 'DevExDim'),
    'human impact (out-of-hours work)': ('well-being', 'Satisf'),
    'ide save events count': ('fine-grained activity events', 'Activity'),
    'ide window activations': ('interruptions / context switches', 'DevExDim'),
    'impact metrics (direct)': ('task completion time', 'ProdPerf'),
    'impact metrics (indirect / dx core 4)': ('experience indices (DXI, rSPACE)', 'DevExDim'),
    'implementation opportunities': ('factors (not metrics)', 'OTHER-factor'),
    'implik (liking - implementation)': ('affect / sentiment', 'Satisf'),
    'imppls (pleasure - implementation)': ('affect / sentiment', 'Satisf'),
    'inclusion of code comments': ('code quality / health', 'Quality'),
    'individual effectiveness': ('perceived productivity (self-report)', 'SurveyPerc'),
    'individual productivity & speed metrics': ('productivity / efficiency score', 'ProdPerf'),
    'industry ai adoption rate': ('tool adoption rate', 'Activity'),
    'innovation strategies': ('factors (not metrics)', 'OTHER-factor'),
    'interaction frequency': ('AI suggestion acceptance / persistence', 'Activity'),
    'interaction frequency (in-code vs chat)': ('AI suggestion acceptance / persistence', 'Activity'),
    'interactive synchronous agents (e.g., claude code)': ('commit count', 'Activity'),
    'intra-team support': ('collaboration / knowledge sharing', 'Collab'),
    'ipip big five personality traits': ('people/capability descriptors', 'OTHER-people'),
    'issue resolution time': ('cycle time', 'Delivery'),
    'job_creativity': ('learning / growth', 'DevExDim'),
    'job_productivity': ('perceived productivity (self-report)', 'SurveyPerc'),
    'knowledge density (\\\\(\\rho(k, \\tau)\\\\))': ('productivity / efficiency score', 'ProdPerf'),
    'knowledge work productivity': ('perceived productivity (self-report)', 'SurveyPerc'),
    'latency (p50 / p90 / end-to-end)': ('model-evaluation metrics', 'OTHER-modeleval'),
    'learning by tinkering': ('people/capability descriptors', 'OTHER-people'),
    'learning resources': ('learning / growth', 'DevExDim'),
    'likelihood of ignoring test failures (sq4.6)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'long-term impact on the code base': ('code quality / health', 'Quality'),
    'mapeamentos de requisitos de privacidade criados': ('task / contribution throughput', 'ProdPerf'),
    'marcadores de seguranca de tipos (type-safety markers)': ('code quality / health', 'Quality'),
    'mean duration of investigation sessions (meandurin-vsess)': ('task completion time', 'ProdPerf'),
    'meaningful work': ('engagement / motivation / retention', 'Satisf'),
    'missed tasks': ('task / contribution throughput', 'ProdPerf'),
    'mutation testing coverage': ('test outcomes (coverage, flakiness)', 'Quality'),
    'métricas de experiência do cliente': ('business/customer metrics', 'OTHER-business'),
    'métricas dora': ('DORA metrics (composite)', 'Delivery'),
    'métricas financeiras e operacionais de ia': ('business/customer metrics', 'OTHER-business'),
    'novel combinations of existing concepts / citations [14]': ('learning / growth', 'DevExDim'),
    'novel reuse of existing libraries [3]': ('learning / growth', 'DevExDim'),
    'novelty (novidade)': ('experience scales (DEXI, AttrakDiff)', 'SurveyPerc'),
    'number of accepted snippets (browser / ai / total)': ('AI suggestion acceptance / persistence', 'Activity'),
    'number of accessibility issues identified during verification': ('defects / rollbacks', 'Quality'),
    'number of contributors': ('collaboration / knowledge sharing', 'Collab'),
    'number of prompts': ('tool adoption rate', 'Activity'),
    'number of refinement cycles required before acceptance': ('rework / technical debt', 'Quality'),
    'number of resolved issues': ('task / contribution throughput', 'ProdPerf'),
    'number of suggestions': ('AI suggestion acceptance / persistence', 'Activity'),
    'office usage frequency / attendance rate': ('work location / attendance (hybrid schedule)', 'Activity'),
    'organizational pressure': ('factors (not metrics)', 'OTHER-factor'),
    'passive rejection / ignored rate (rejeição passiva / ignoradas)': ('AI suggestion acceptance / persistence', 'Activity'),
    'peer feedback (limited scope) [9]': ('performance rating', 'ProdPerf'),
    'perceived ability (accomplishing new tasks)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'perceived ai competence': ('trust in AI tools', 'SurveyPerc'),
    'perceived code editing frequency': ('survey / psychometric instrument', 'SurveyPerc'),
    'perceived code error rate': ('trust in AI tools', 'SurveyPerc'),
    'perceived code readability': ('code quality / health', 'Quality'),
    'perceived code reuse frequency': ('survey / psychometric instrument', 'SurveyPerc'),
    'perceived distraction (distração percebida)': ('interruptions / context switches', 'DevExDim'),
    'perceived disturbance / disruptiveness': ('interruptions / context switches', 'DevExDim'),
    'perceived diversity & inclusion (d&i percebida) [2, 24]': ('factors (not metrics)', 'OTHER-factor'),
    'perceived helpfulness (utilidade percebida)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'perceived impact of challenges (24 challenges)': ('factors (not metrics)', 'OTHER-factor'),
    'perceived individual productivity': ('perceived productivity (self-report)', 'SurveyPerc'),
    'perceived room odor rating': ('factors (not metrics)', 'OTHER-factor'),
    'perceived strenuousness of coding without acat': ('perceived workload', 'SurveyPerc'),
    'perceived task difficulty': ('perceived workload', 'SurveyPerc'),
    'perceived task difficulty (1–5 scale)': ('perceived workload', 'SurveyPerc'),
    'perceived team productivity (on-time delivery, high quality, team effectiveness)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'percentage of code created by human vs. ai': ('AI suggestion acceptance / persistence', 'Activity'),
    'percentage of comments': ('code quality / health', 'Quality'),
    'physical absences / room attendance': ('work location / attendance (hybrid schedule)', 'Activity'),
    'pipeline automated tests success rate (m09)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'pipeline duration': ('build count / time', 'Activity'),
    'pipeline frequency': ('build count / time', 'Activity'),
    'pipeline success rate': ('build success rate', 'Quality'),
    'post-task subjective experience ratings': ('survey / psychometric instrument', 'SurveyPerc'),
    'presence of hard forks': ('collaboration / knowledge sharing', 'Collab'),
    'principais preocupacoes com ai': ('trust in AI tools', 'SurveyPerc'),
    'production downtime issues': ('incidents / instability', 'Quality'),
    'productive when coding ("i feel productive when i code") [8, 9]': ('perceived productivity (self-report)', 'SurveyPerc'),
    'productivity & speed metrics': ('productivity / efficiency score', 'ProdPerf'),
    'produtividade percebida': ('perceived productivity (self-report)', 'SurveyPerc'),
    'program comprehension allocation (xia et al.)': ('comprehension tasks', 'SurveyPerc'),
    'programming language': ('factors (not metrics)', 'OTHER-factor'),
    'programming productivity (y)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'progress / evolution': ('perceived productivity (self-report)', 'SurveyPerc'),
    'prompt crafting success rate [22]': ('AI suggestion acceptance / persistence', 'Activity'),
    'prompt volume & triggers': ('tool adoption rate', 'Activity'),
    'proportion of unclosed tickets': ('task / contribution throughput', 'ProdPerf'),
    'qualidade da base de código': ('code quality / health', 'Quality'),
    'qualidade de software e defeitos': ('defects / rollbacks', 'Quality'),
    'qualitative creative moments / screenshots [5, 15]': ('learning / growth', 'DevExDim'),
    'quality (q)': ('code quality / health', 'Quality'),
    'quality in use: beneficialness (usability, accessibility, suitability)': ('perceived usability / learnability', 'SurveyPerc'),
    'quality in use: freedom from risk & acceptability (trust, safety, compliance)': ('trust in AI tools', 'SurveyPerc'),
    'quality of recommendations': ('AI suggestion acceptance / persistence', 'Activity'),
    'quality of social interactions': ('affect / sentiment', 'Satisf'),
    'quality requirements': ('factors (not metrics)', 'OTHER-factor'),
    'quantity of delivered tasks / quantidade de tarefas entregues': ('task / contribution throughput', 'ProdPerf'),
    'quantity of recommendations': ('AI suggestion acceptance / persistence', 'Activity'),
    'ratio of contributing forks': ('collaboration / knowledge sharing', 'Collab'),
    'read versus write time': ('fine-grained activity events', 'Activity'),
    'reducao no tempo de escrita de codigo (writing code)': ('task completion time', 'ProdPerf'),
    'release cycle compression (\\\\(\\delta\\tau\\\\))': ('release frequency / time to market', 'Delivery'),
    'release success rate / successful releases (d09)': ('change failure rate', 'Quality'),
    'requirement implementation correctness (% of correct features)': ('task correctness (experiments)', 'ProdPerf'),
    'requirements compliance': ('task correctness (experiments)', 'ProdPerf'),
    'requirements implemented per minute (task speed)': ('task / contribution throughput', 'ProdPerf'),
    'resource utilization (storage space)': ('business/customer metrics', 'OTHER-business'),
    'resumption lag': ('interruptions / context switches', 'DevExDim'),
    'review & pipeline metrics': ('code-review interaction', 'Collab'),
    'risk tolerance': ('people/capability descriptors', 'OTHER-people'),
    'role-based deliveries': ('task / contribution throughput', 'ProdPerf'),
    'saccade count': ('physiological / cognition measures', 'SurveyPerc'),
    'sample entropy (candidate)': ('work location / attendance (hybrid schedule)', 'Activity'),
    'satisfied with job ("i feel satisfied with my job") [8, 9, 12]': ('satisfaction', 'Satisf'),
    'save-to-edit ratio': ('fine-grained activity events', 'Activity'),
    'schwartz value inventory': ('survey / psychometric instrument', 'SurveyPerc'),
    'searches for information online ("searching for information and resources online is a central part of my job") [8, 9]': ('DevEx driver items (survey)', 'DevExDim'),
    'selective information processing': ('people/capability descriptors', 'OTHER-people'),
    'self vision': ('perceived productivity (self-report)', 'SurveyPerc'),
    'self-sufficiency': ('interruptions / context switches', 'DevExDim'),
    'sense of ownership of work': ('engagement / motivation / retention', 'Satisf'),
    'service level agreements (slas) and objectives (slos) (m15)': ('incidents / instability', 'Quality'),
    'similarity to correct code': ('task correctness (experiments)', 'ProdPerf'),
    'skin temperature': ('physiological / cognition measures', 'SurveyPerc'),
    'software releases increase': ('release frequency / time to market', 'Delivery'),
    'software reuse level (nivel de reuso de software)': ('survey / psychometric instrument', 'SurveyPerc'),
    'software size (unadjusted fp)': ('effort / size estimates', 'ProdPerf'),
    'speed (s)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'speed, ease, and quality': ('experience indices (DXI, rSPACE)', 'DevExDim'),
    'startup cost (custo fixo de início de leitura)': ('physiological / cognition measures', 'SurveyPerc'),
    'state transition probabilities': ('fine-grained activity events', 'Activity'),
    'state transition probability & entropy rate [5, 26, 27]': ('fine-grained activity events', 'Activity'),
    'static analysis warnings': ('code quality / health', 'Quality'),
    'subjective accuracy': ('trust in AI tools', 'SurveyPerc'),
    'subjective productivity': ('perceived productivity (self-report)', 'SurveyPerc'),
    'subjective productivity rating': ('perceived productivity (self-report)', 'SurveyPerc'),
    'suggestion duration (tempo de exibição da sugestão)': ('AI suggestion acceptance / persistence', 'Activity'),
    'surfacing requirements (q8)': ('DevEx driver items (survey)', 'DevExDim'),
    'survival rate of accepted code (10-min survival) [20]': ('AI suggestion acceptance / persistence', 'Activity'),
    'switch count / switch frequency': ('interruptions / context switches', 'DevExDim'),
    'system stability & quality metrics': ('incidents / instability', 'Quality'),
    'task accuracy': ('task correctness (experiments)', 'ProdPerf'),
    'task correctness rate': ('task correctness (experiments)', 'ProdPerf'),
    'task difficulty (dificuldade da tarefa)': ('perceived workload', 'SurveyPerc'),
    'task enjoyment rating': ('affect / sentiment', 'Satisf'),
    'task meaningfulness': ('engagement / motivation / retention', 'Satisf'),
    'task speedup / completion time': ('task completion time', 'ProdPerf'),
    'taxa de adocao e produtividade percebida': ('tool adoption rate', 'Activity'),
    'taxa de duplicacao de codigo (jscpd 4.x)': ('code quality / health', 'Quality'),
    'taxa e contagem de reversoes (reverts)': ('defects / rollbacks', 'Quality'),
    'team dynamics & peer feedback': ('collaboration / knowledge sharing', 'Collab'),
    'team size': ('people/capability descriptors', 'OTHER-people'),
    'team size / active developers': ('people/capability descriptors', 'OTHER-people'),
    'team stability index (\\\\(tsi^{-1}\\\\))': ('engagement / motivation / retention', 'Satisf'),
    'team vision': ('performance rating', 'ProdPerf'),
    'teamwork quality': ('collaboration / knowledge sharing', 'Collab'),
    'tech debt impact': ('rework / technical debt', 'Quality'),
    'technical quality / qualidade técnica': ('code quality / health', 'Quality'),
    'technology used': ('factors (not metrics)', 'OTHER-factor'),
    'tempo de conclusao de tarefa (time-to-completion)': ('task completion time', 'ProdPerf'),
    'tempo de reinicialização do servidor/container (server restart time)': ('feedback loops', 'DevExDim'),
    'tempo de setup (setup time)': ('onboarding / mentoring', 'Collab'),
    'teslik (liking - testing)': ('affect / sentiment', 'Satisf'),
    'tespls (pleasure - testing)': ('affect / sentiment', 'Satisf'),
    'test latency': ('feedback loops', 'DevExDim'),
    'test quality': ('test outcomes (coverage, flakiness)', 'Quality'),
    'testing confidence loss rating (sq4.4)': ('test outcomes (coverage, flakiness)', 'Quality'),
    'ticket_difficulty': ('DevEx driver items (survey)', 'DevExDim'),
    'ticket_granularity': ('DevEx driver items (survey)', 'DevExDim'),
    'time lost to obstacles': ('task completion time', 'ProdPerf'),
    'time to accept / onscreen display duration [14, 18-20]': ('AI suggestion acceptance / persistence', 'Activity'),
    'time to completion & time to success': ('task completion time', 'ProdPerf'),
    'time to first working draft': ('task completion time', 'ProdPerf'),
    'time to hello world': ('onboarding / mentoring', 'Collab'),
    'time-to-completion': ('task completion time', 'ProdPerf'),
    'timebox / deadline adherence': ('sprint / iteration metrics', 'Agile'),
    'timeliness (pontualidade/prazos)': ('performance rating', 'ProdPerf'),
    'tool adoption & trust percentages': ('tool adoption rate', 'Activity'),
    'tool preference / future adoption intent': ('perceived usability / learnability', 'SurveyPerc'),
    'tool usability': ('DevEx driver items (survey)', 'DevExDim'),
    'tool usage indicator (binary)': ('tool adoption rate', 'Activity'),
    'total time to acceptable completion': ('task completion time', 'ProdPerf'),
    'triage override / precision rate': ('model-evaluation metrics', 'OTHER-modeleval'),
    'trust & reliance (over/under-reliance)': ('trust in AI tools', 'SurveyPerc'),
    'trust & transparency': ('trust in AI tools', 'SurveyPerc'),
    'trust in accuracy': ('trust in AI tools', 'SurveyPerc'),
    'trust in ai': ('trust in AI tools', 'SurveyPerc'),
    'ttct scores (fluency, flexibility, originality, elaboration)': ('learning / growth', 'DevExDim'),
    'typed characters': ('fine-grained activity events', 'Activity'),
    'unowned repositories count': ('collaboration / knowledge sharing', 'Collab'),
    'usefulness (utilidade)': ('perceived productivity (self-report)', 'SurveyPerc'),
    'user interaction click rate': ('fine-grained activity events', 'Activity'),
    'usuários ativos semanais (weekly active users - wau)': ('tool adoption rate', 'Activity'),
    'utilization metrics': ('tool adoption rate', 'Activity'),
    'velocidade de digitação (typing speed)': ('fine-grained activity events', 'Activity'),
    'verification & sgm execution metrics': ('test outcomes (coverage, flakiness)', 'Quality'),
    'visited websites count': ('fine-grained activity events', 'Activity'),
    'visual analogue scale (vas) — perceived pain of gender barriers [8, 9]': ('factors (not metrics)', 'OTHER-factor'),
    'visual description confidence': ('trust in AI tools', 'SurveyPerc'),
    'volume': ('AI suggestion acceptance / persistence', 'Activity'),
    'volume of accepted characters (browser / ai / total)': ('AI suggestion acceptance / persistence', 'Activity'),
    'volume of code added and omitted': ('lines of code changed', 'Activity'),
    'website visits (productive vs. distracting)': ('fine-grained activity events', 'Activity'),
    'weekly markov consistency': ('work location / attendance (hybrid schedule)', 'Activity'),
    'work capacity': ('story points completed', 'ProdPerf'),
    'work capacity (\\\\(w_i\\\\))': ('story points completed', 'ProdPerf'),
    'work day length': ('work hours / active time', 'Activity'),
    'work environmental conditions': ('factors (not metrics)', 'OTHER-factor'),
    'work location (office vs. wfh vs. non-work day)': ('work location / attendance (hybrid schedule)', 'Activity'),
    'work quality (qualidade do trabalho)': ('code quality / health', 'Quality'),
    'work vision': ('perceived productivity (self-report)', 'SurveyPerc'),
}
NONMETRIC_UPDATE = {
    'avaliação dos princípios de design (dp evaluation: accessibility, importance, novelty, actability, effectiveness)',
    'data saturation index [6]',
    'developer study sample size',
    'development platform',
    'development type',
    'enterprise size threshold (<200 developers)',
    'erosao na developer experience (negative cohort)',
    'escopo e amostra da pesquisa',
    'finding agreement rating',
    'governance specification baseline in literature',
    'multilayer neural network model (candidate)',
    'métricas de governança e alinhamento',
    'production metrics',
    'propensity score & average treatment effect',
    'reddit thread score',
    'traditional metrics (critiqued)',
}
CURATED.update(CURATED_UPDATE)
# D1 recovery 2026-10-19: curation of the metric names of the 8 sources recovered and included (assistant draft, approved by the author)
CURATED_D1 = {
    'access-driven usage intention (b6)': ('perceived usability / learnability', 'SurveyPerc'),
    'access-driven willingness (b7)': ('perceived usability / learnability', 'SurveyPerc'),
    'add-on options variety (c4)': ('DevEx driver items (survey)', 'DevExDim'),
    'ai spend [24, 38]': ('business/customer metrics', 'OTHER-business'),
    'ai tool adoption rate [31]': ('tool adoption rate', 'Activity'),
    'anti-innovation time factors': ('inner/outer-loop time', 'Agile'),
    'atmosphere': ('factors (not metrics)', 'OTHER-factor'),
    'attractiveness (e2)': ('experience scales (DEXI, AttrakDiff)', 'SurveyPerc'),
    'bad developer days': ('experience indices (DXI, rSPACE)', 'DevExDim'),
    'build & ci regression metrics': ('build success rate', 'Quality'),
    'commitment': ('engagement / motivation / retention', 'Satisf'),
    'confidence': ('psychometric scales (CIPS, S-SCS)', 'Satisf'),
    'convenience (c3)': ('perceived usability / learnability', 'SurveyPerc'),
    'dau / wau / mau for ai tools [22, 38]': ('tool adoption rate', 'Activity'),
    'decision power': ('factors (not metrics)', 'OTHER-factor'),
    'developer friction score [25, 41]': ('DevEx driver items (survey)', 'DevExDim'),
    'diff authoring time [40, 41]': ('task completion time', 'ProdPerf'),
    'ease of delivery [25, 41]': ('DevEx driver items (survey)', 'DevExDim'),
    'effective working hours / work duration ratio': ('work hours / active time', 'Activity'),
    'felt value (e4)': ('affect / sentiment', 'Satisf'),
    'frequency of ai use (frequency of daily/weekly ai tool usage)': ('tool adoption rate', 'Activity'),
    'goal setting': ('sprint / iteration metrics', 'Agile'),
    'higher-price usage intention (b1)': ('perceived usability / learnability', 'SurveyPerc'),
    'improving the process': ('sprint / iteration metrics', 'Agile'),
    'information value quality (c5)': ('DevEx driver items (survey)', 'DevExDim'),
    'innovation time ratio': ('inner/outer-loop time', 'Agile'),
    'intrigue (e1)': ('affect / sentiment', 'Satisf'),
    'learning from failures': ('learning / growth', 'DevExDim'),
    'mean-high model contribution rate (mhmcr)': ('task / contribution throughput', 'ProdPerf'),
    'organizational learning': ('collaboration / knowledge sharing', 'Collab'),
    'peer feedback / colleague assessment': ('collaboration / knowledge sharing', 'Collab'),
    'perceived ease of delivery': ('DevEx driver items (survey)', 'DevExDim'),
    'percentage of ai-written code [38, 42]': ('AI suggestion acceptance / persistence', 'Activity'),
    'platform speed (c8)': ('DevEx driver items (survey)', 'DevExDim'),
    'positive feeling (e3)': ('affect / sentiment', 'Satisf'),
    'pride': ('satisfaction', 'Satisf'),
    'psip progress scores (0–5 scale)': ('sprint / iteration metrics', 'Agile'),
    're-use intention (b5)': ('perceived usability / learnability', 'SurveyPerc'),
    'requirements handling by the team': ('sprint / iteration metrics', 'Agile'),
    'resource value quality (c6)': ('DevEx driver items (survey)', 'DevExDim'),
    'stability (c2)': ('DevEx driver items (survey)', 'DevExDim'),
    'team capacity': ('sprint / iteration metrics', 'Agile'),
    'team leader': ('factors (not metrics)', 'OTHER-factor'),
    'team setup': ('people/capability descriptors', 'OTHER-people'),
    'teamwide ai adoption level (proportion of team members using ai)': ('tool adoption rate', 'Activity'),
    'technology value quality (c7)': ('DevEx driver items (survey)', 'DevExDim'),
    'thriving score': ('engagement / motivation / retention', 'Satisf'),
    'understanding job roles': ('factors (not metrics)', 'OTHER-factor'),
    'usage intention (b2)': ('perceived usability / learnability', 'SurveyPerc'),
    'usage plan (b3)': ('perceived usability / learnability', 'SurveyPerc'),
    'willingness to pay additional cost (b4)': ('perceived usability / learnability', 'SurveyPerc'),
}
NONMETRIC_UPDATE |= {
    'developer productivity & sustainability metrics',
}
CURATED.update(CURATED_D1)


def main():
    rows = harvest()
    canon, nonmetric, still = [], [], []
    for sid, raw in rows:
        c = clean(raw)
        if not c or len(c) < 3:
            continue
        if NONMETRIC.search(c) or c in NONMETRIC_UPDATE:
            nonmetric.append((sid, c))
            continue
        if c in CURATED:
            name, cat = CURATED[c]
            canon.append((sid, name, cat))
            continue
        for rx, name, cat in RULES:
            if re.search(rx, c):
                canon.append((sid, name, cat))
                break
        else:
            still.append((sid, c))
    for sid, lst in MANUAL.items():
        for name, cat in lst:
            canon.append((sid, name, cat))

    agg = defaultdict(set)
    for sid, name, cat in canon:
        agg[(cat, name)].add(sid)
    with open(OUT / 'metric_inventory.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['category', 'metric', 'n_sources', 'academic', 'grey', 'sources'])
        for (cat, name), sids in sorted(agg.items(), key=lambda kv: (kv[0][0], -len(kv[1]))):
            acad = sum(1 for s in sids if s.startswith('P'))
            w.writerow([cat, name, len(sids), acad, len(sids) - acad, ';'.join(sorted(sids))])
    with open(OUT / 'metric_inventory_unclassified.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['source', 'raw_metric'])
        w.writerows(still)
    with open(OUT / 'metric_inventory_nonmetric.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['source', 'raw_item'])
        w.writerows(nonmetric)

    tot = len(canon) + len(still) + len(nonmetric)
    src_cov = len({s for s, _, _ in canon})
    print(f'instances: {tot} | classified: {len(canon)} ({100*len(canon)/tot:.0f}%) | '
          f'non-metrics excluded: {len(nonmetric)} | residue: {len(still)} ({100*len(still)/tot:.0f}%)')
    print(f'sources covered: {src_cov}')


if __name__ == '__main__':
    main()
