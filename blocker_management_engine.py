# Blocker Management Engine
# Identify, track, and resolve critical blockers for Release 4.2

import pandas as pd

class BlockerManagementEngine:
    def __init__(self):
        self.blocker_types = {
            'VAT country code mismatch': 'Tax/Compliance',
            'Legacy export file pending': 'Data Migration',
            'acmemock02.de training access': 'Training',
            'Legacy export delimiter mismatch': 'Data Migration',
            'UAT performance tuning': 'Performance',
            'Release 4.2 cutover window': 'Release'
        }
        self.customers = ['BluePeak', 'Meridian', 'UrbanNest', 'NordForge', 'ClearWave', 'Helio']
    
    def identify_blockers(self, rollout_df):
        '''Identify all critical blockers'''
        blockers = []
        for idx, row in rollout_df.iterrows():
            blocker_text = row.get('Critical Blockers', '')
            if pd.notna(blocker_text) and blocker_text != '':
                blocker_type = self.blocker_types.get(blocker_text, 'Unknown')
                blockers.append({
                    'customer': row['Customer'],
                    'phase': row['Phase'],
                    'blocker': blocker_text,
                    'type': blocker_type,
                    'milestone': row['Milestone'],
                    'dependency': row.get('Blocking Dependency', ''),
                    'readiness': row['Readiness %']
                })
        return blockers
    
    def blocker_impact(self, rollout_df):
        '''Assess blocker impact by type'''
        impact = {}
        blockers = self.identify_blockers(rollout_df)
        
        for blocker in blockers:
            btype = blocker['type']
            if btype not in impact:
                impact[btype] = {'count': 0, 'customers': [], 'severity': 'High'}
            impact[btype]['count'] += 1
            if blocker['customer'] not in impact[btype]['customers']:
                impact[btype]['customers'].append(blocker['customer'])
        
        return impact
    
    def customer_blockers(self, rollout_df):
        '''Blockers by customer'''
        cust_blockers = {}
        blockers = self.identify_blockers(rollout_df)
        
        for customer in self.customers:
            cust_blockers[customer] = [b for b in blockers if b['customer'] == customer]
        
        return cust_blockers
    
    def mitigation_plan(self, blocker_type):
        '''Suggest mitigation for blocker type'''
        plans = {
            'Tax/Compliance': 'Schedule EU VAT mapping workshop, configure override',
            'Data Migration': 'Coordinate with legacy vendor, standardize delimiters',
            'Training': 'Fix training tenant access, complete certification',
            'Performance': 'Run performance tuning, UAT verification',
            'Release': 'Coordinate release cutover window with all teams'
        }
        return plans.get(blocker_type, 'Escalate to sponsor')

if __name__ == "__main__":
    engine = BlockerManagementEngine()
    print("Blocker Management Engine v1.0 initialized")
    print("Blocker types: Tax, Data Migration, Training, Performance, Release")
