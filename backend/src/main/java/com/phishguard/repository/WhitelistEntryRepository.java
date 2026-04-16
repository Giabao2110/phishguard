package com.phishguard.repository;

import com.phishguard.model.entity.WhitelistEntry;
import org.springframework.data.jpa.repository.JpaRepository;

public interface WhitelistEntryRepository extends JpaRepository<WhitelistEntry, Long> {
    boolean existsByEntryValue(String entryValue);
}
