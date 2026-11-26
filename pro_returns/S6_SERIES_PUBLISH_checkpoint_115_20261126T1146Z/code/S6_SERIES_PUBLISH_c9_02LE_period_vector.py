#!/usr/bin/env python3
"""Prepare the exact final LE period-vector naming fragment; no canonical writes."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet
from S6_SERIES_PUBLISH_c9_notation_addendum_io import stage

p = Packet('02LE', 'maps:src:D.2.38',
           'dbf99af3b3e5e721810dc3bb21da3d646d14c2d994346c8e4471ff8ae836fea7',
           '457–473', 'Marked period vector and multiplicative chart coordinate.')
p.scope('marked-period-vector',
        r'Positive $\gamma$ is the actual forward period covering $-Q$.',
        'Every entry is integral;',
        p.literals([(r'$z=', r'$z_{\rm per}=', 2),
                    (r'\beta(bz)', r'\beta(bz_{\rm per})', 2),
                    (r'Put $c=', r'Put $c_{\rm per}=', 1),
                    (r'g-c\\', r'g-c_{\rm per}\\', 1)]),
        'The same marked rational period vector is now z_per=(A-I)^(-1)g at a finite elliptic site and z_per=(kappa/n)v at I_n. The identity on its two coordinates, with inverse restoring the earlier vector name, preserves beta(b z_per), hence the complete displayed T. The period scalar c_per=beta(b z_per)+w has exactly the old scalar value, with inverse c=c_per in these two period-matrix uses. T^(-1) therefore retains lower-left entry -beta A^(-1) and lower-right entry b beta A^(-1)g-c_per; both matrix products have exactly the original entries. All four vector occurrences and both period-scalar occurrences are changed, including both concatenated bz products. The earlier residual c=b/product(q_i), retained at c=10,14, keeps its original values and name. The later physical chart coordinate remains z=exp(2 pi i z_E), with its stated logarithm modulo the short period; its line actions, gauges and reciprocals are unchanged. This supersedes the old retention based only on separate period and chart paragraphs, without changing any geometric map.')
stage([p], 'S6_SERIES_PUBLISH_c9_02LE_period_vector',
      'continuation9_02LE_period_vector', 'period_vector',
      'The actual marked period vector is qualified in both definitions and both scalar entries; the independent period scalar is qualified in its definition and inverse entry. The full period matrix and its inverse, physical exponential/logarithm, line maps and all numerical assertions are preserved.')
